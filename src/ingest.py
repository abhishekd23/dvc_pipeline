import streamlit as st
import os
import torch
from PIL import Image
import glob
import zipfile
import yaml 

params = yaml.safe_load(open('params.yaml'))['prepare']

count = params['count']

data = os.path.join('data','prepared','v{}'.format(params['count']))
origimg_path = os.path.join('data', 'store', f"v{params['count']}")
# print(data_path)
os.makedirs(data, exist_ok=True)
os.makedirs(origimg_path, exist_ok=True)

with zipfile.ZipFile(f'buffer/dataset{params["count"]}.zip',"r") as zipf:
    zipf.extractall(data)
    zipf.extractall(origimg_path)
