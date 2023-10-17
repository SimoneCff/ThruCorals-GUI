from __future__ import absolute_import, division, print_function
from SeaThru.Transform.monodepth2.utils import download_model_if_doesnt_exist
import rawpy
import PIL.Image as pil
import torch
from torchvision import transforms
from .Transform.monodepth2.networks import ResnetEncoder, DepthDecoder
from .Transform.seathru import *
import os
import warnings

os.environ['KMP_DUPLICATE_LIB_OK']='True' 

warnings.simplefilter('ignore')

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def run(image_name, model_path ,bright, balance, illum, min, max, fract, add, mul, size, rawn, out):
    """Function to predict for a single image or folder of images
    """

    device = torch.device("cpu")
   
    download_model_if_doesnt_exist("mono+stereo_1024x320")
    encoder_path = os.path.join(model_path, "encoder.pth")
    depth_decoder_path = os.path.join(model_path, "depth.pth")

    # LOADING PRETRAINED MODEL
    encoder = ResnetEncoder(18, False)
    loaded_dict_enc = torch.load(encoder_path, map_location=device, weights_only=False)

    # extract the height and width of image that this model was trained with
    feed_height = loaded_dict_enc['height']
    feed_width = loaded_dict_enc['width']
    filtered_dict_enc = {k: v for k, v in loaded_dict_enc.items() if k in encoder.state_dict()}
    encoder.to(device)
    encoder.load_state_dict(filtered_dict_enc)
    encoder.eval()

    depth_decoder = DepthDecoder(
        num_ch_enc=encoder.num_ch_enc, scales=range(4))

    loaded_dict = torch.load(depth_decoder_path, map_location=device)
    depth_decoder.load_state_dict(loaded_dict)

    depth_decoder.to(device)
    depth_decoder.eval()


    # Load image and preprocess
    img = Image.fromarray(rawpy.imread(+image_name).postprocess()) if image_name.endswith(".raw") else pil.open(image_name).convert('RGB')
    img.thumbnail((size, size), Image.ANTIALIAS)
    original_width, original_height = img.size
    input_image = img.resize((feed_width, feed_height), pil.LANCZOS)
    input_image = transforms.ToTensor()(input_image).unsqueeze(0)

    # PREDICTION
    input_image = input_image.to(device)
    features = encoder(input_image)
    outputs = depth_decoder(features)

    disp = outputs[("disp", 0)]
    disp_resized = torch.nn.functional.interpolate(
        disp, (original_height, original_width), mode="bilinear", align_corners=False)

    # Saving colormapped depth image
    disp_resized_np = disp_resized.squeeze().cpu().detach().numpy()
    mapped_im_depths = ((disp_resized_np - np.min(disp_resized_np)) / (
            np.max(disp_resized_np) - np.min(disp_resized_np))).astype(np.float32)
    depths = preprocess_monodepth_depth_map(mapped_im_depths, add,mul)
    recovered = run_pipeline(np.array(img) / 255.0, depths, min,bright,illum,fract,balance)
    # recovered = exposure.equalize_adapthist(scale(np.array(recovered)), clip_limit=0.03)
    sigma_est = estimate_sigma(recovered, average_sigmas=True) / 10.0
    recovered = denoise_tv_chambolle(recovered, sigma_est)
    im = Image.fromarray((np.round(recovered * 255.0)).astype(np.uint8))

    image_name = os.path.basename(image_name)
    output = os.path.join(out,image_name)
    im.save(output, format='jpeg')