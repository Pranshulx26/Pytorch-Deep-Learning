"""Checks if the data directory exist if not create it and download the data 
from Github Repository.
"""
import os 
import zipfile 
import requests
from pathlib import Path 


def download_data(source: str, destination: str):
    # Setup path to data folder
    data_path = Path('data/')
    image_path = data_path / destination
    
    # If the image folder doesn't exist, download it and prepare it 
    if image_path.is_dir():
        print(f'{image_path} directory exists...')
    else:
        print(f'Did not find {image_path} directory, creating one...')
        image_path.mkdir(parents=True, exist_ok=True)
    
        # Downloading data
        with open(data_path / 'pizza_steak_sushi.zip', 'wb') as f:
            request = requests.get(source)
            print('Downloading pizza, steak, sushi data.....')
            f.write(request.content)
        
        # Unzip pizza, steak, sushi data 
        with zipfile.ZipFile(data_path/'pizza_steak_sushi.zip', 'r') as zip_ref:
            print('Unzipping pizza, steak, sushi data.....')
            zip_ref.extractall(image_path)
        
        # Remove zip file 
        os.remove(data_path / 'pizza_steak_sushi.zip')
    return image_path
