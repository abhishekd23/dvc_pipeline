import streamlit as st
import os
import torch
from PIL import Image
import glob
import zipfile
import yaml 

params = yaml.safe_load(open('params.yaml'))['prepare']

count = params['count']

data = os.path.join('data','prepared','v{}'.format(params['count']),'images')
origimg_path = os.path.join('data', 'store', 'v{}'.format(params['count']))
# print(data_path)
os.makedirs(data, exist_ok=True)
os.makedirs(origimg_path, exist_ok=True)

with zipfile.ZipFile(f'/home/bdz1kor/dvc_pipeline/buffer/dataset{params["count"]}.zip',"r") as zipf:
    print(params['count'])
    zipf.extractall(data)
    zipf.extractall(origimg_path)
    