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


<<<<<<< HEAD
        os.makedirs('storage',exist_ok=True)
        for ff in os.listdir('storage'):
            os.remove(f'storage/{ff}')
    
        with open(f'storage/dataset{params["count"]+1}.zip', "wb") as f:
=======
        for ff in os.listdir('buffer'):
            os.remove(f'buffer/{ff}')
    
        with open(f'buffer/dataset{params["count"]+1}.zip', "wb") as f:
>>>>>>> 39890c1... dvc
            f.write(imgs.getbuffer())

        

        if not os.system("dvc repro"):
<<<<<<< HEAD
            imgname = os.listdir("data/store/v{}/predictions".format(params["count"]+1))
            preds = glob.glob("data/store/v{}/predictions/*.*".format(params["count"]+1), recursive=True)
=======
            imgname = os.listdir("data/store/v{}/predictions".format(params["dcount"]+1))
            preds = glob.glob("data/store/v{}/predictions/*.*".format(params["dcount"]+1), recursive=True)
>>>>>>> 39890c1... dvc
            for index,im in enumerate(preds):
                st.image(im, imgname[index])
            print('done')
    
    else: 
        return 



<<<<<<< HEAD
=======
    # imgname = os.listdir("dataset/v{}".format(st.session_state['dcount']))
    # preds = glob.glob("dataset/v{}/*.*".format(st.session_state['dcount']), recursive=True)

    # results = model(preds)
    # results.imgs
    # results.render()
    # os.mkdir("output/v{}".format(st.session_state['dcount']))
    # for index,im in enumerate(results.imgs):
        
    #     img = Image.fromarray(im)
    #     img.save('output/v{}/{}'.format(st.session_state['dcount'], imgname[index]))

    #     st.image('output/v{}/{}'.format(st.session_state['dcount'], imgname[index]))

    # st.button('Predict')

>>>>>>> 39890c1... dvc
if __name__ == '__main__':
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, _verbose=False)
    # model.classes = [0]
    main()