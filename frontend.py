import streamlit as st
import os
import torch
from PIL import Image
import glob
import zipfile
import yaml

def main():
    st.title('Test Predict YoloV5')
    imgs = st.file_uploader("Choose Images")


    if imgs:
        params = yaml.safe_load(open('params.yaml'))['prepare']
        update_count = {'prepare':{'count':params['count']+1}}
        yaml.dump(update_count,open('params.yaml','w'))


        os.makedirs('storage',exist_ok=True)
        for ff in os.listdir('storage'):
            os.remove(f'storage/{ff}')
    
        with open(f'storage/dataset{params["count"]+1}.zip', "wb") as f:
            f.write(imgs.getbuffer())

        

        if not os.system("dvc repro"):
            imgname = os.listdir("data/store/v{}/predictions".format(params["count"]+1))
            preds = glob.glob("data/store/v{}/predictions/*.*".format(params["count"]+1), recursive=True)
            for index,im in enumerate(preds):
                st.image(im, imgname[index])
            print('done')
    
    else: 
        return 



if __name__ == '__main__':
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, _verbose=False)
    # model.classes = [0]
    main()