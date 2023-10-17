import os
import torch
import torchvision.transforms as transforms
from .CNN import CoralCNN
import pandas as pd
from PIL import Image
from .delete import delete

batch_size =  256
rsize = (244, 244)

def read_csv(classes):
    tmp = []
    data_df = pd.read_csv(classes)
    for index, row in data_df.iterrows():
        tmp.append(row['class_name'])
    return tmp


def Smart_sorting(dir,image_i):
    labels = read_csv('CNN/classes.csv')
    delete()

    # Transform Function
    transform = transforms.Compose([
        transforms.Resize(rsize),  # Ridimensiona l'immagine a 256x256 pixel
        transforms.ToTensor(),  # Converti l'immagine in un tensore PyTorch
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalizza i valori dei pixel
    ])
    # CNN
    model = CoralCNN(num_classes=72)

    if not torch.cuda.is_available():
        checkpoint = torch.load('CNN/checkpoint.pth',map_location=torch.device('cpu'))
    else:
        checkpoint = torch.load('CNN/checkpoint.pth')
    model.load_state_dict(checkpoint['model_state_dict'])

    # Test the model
    model.eval()  # Set the model to evaluation mode

    # Ciclo sui file nella cartella
    delete()
    # Crea il percorso completo del file
    file_path = os.path.join(dir,image_i)
    
    # Carica e preelabora l'immagine
    image = Image.open(file_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)
    
    # Esegui l'inferenza sulla SeaCNN
    with torch.no_grad():
        output = model(image_tensor)
    
    # Ottieni l'etichetta della classe predetta
    _, predicted_idx = torch.max(output, 1)
    predicted_label = labels[predicted_idx.item()]

    # Crea la cartella per l'etichetta della classe
    output_folder = os.path.join(dir, str(predicted_label))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Crea il percorso completo per il nuovo file
    output_file_path = os.path.join(output_folder, os.path.basename(file_path))

    # Salva l'immagine nella cartella corrispondente
    image.save(output_file_path)
    os.remove(file_path)

    delete()
    return str(predicted_label)
