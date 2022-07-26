from cProfile import label
import torch
import sys
import os
from PIL import Image
import yaml
import glob
import pandas as pd
import cv2

if len(sys.argv) != 4:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write(
        '\tpython3 src/predict.py data/prepared data/predictions data/store\n'
    )
    sys.exit(1)

params = yaml.safe_load(open('params.yaml'))['prepare']

data_path = os.path.join(sys.argv[1], "v{}".format(params['count']), 'images')
predict_path = os.path.join(sys.argv[2], "v{}".format(params['count']), 'images')
origpred = os.path.join(sys.argv[3], "v{}".format(params['count']), 'predictions')
pred_path = os.path.join(sys.argv[2], "v{}".format(params['count']))

print(predict_path)
print(data_path)

os.makedirs(predict_path, exist_ok=True)
os.makedirs(origpred, exist_ok=True)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, _verbose =False )
img = os.path.join(data_path, os.listdir(data_path)[0])

preds = glob.glob(f'{data_path}/*.jpg', recursive=True)
labels = os.listdir(data_path)

information={'xmin':[],'ymin':[],'xmax':[],'ymax':[],'name':[] ,'label':[], 'image':[]}
for images in os.listdir(data_path):
    img = cv2.imread(os.path.join(data_path,images))
    pred = model(img)
    pred.render()
    im = pred.imgs
    image = Image.fromarray(im)
    df = pred.pandas().xyxyn[0]
    res = df[df["name"]=="person"]
    image.save(f'{origpred}/{images}')
    for index, yolo_bb in res.iterrows():
        #file_name = images.split('/')[-1][0:-4]
        information['name']+= [images]
        information['label']+= [yolo_bb['name']]
        information['xmin']+= [yolo_bb["xmin"]*img.shape[1]]
        information['xmax']+= [yolo_bb["xmax"]*img.shape[1]]
        information['ymin']+= [yolo_bb["ymin"]*img.shape[0]]
        information['ymax']+= [yolo_bb["ymax"]*img.shape[0]]
        information['image']+= [f'{origpred}/{images}']

# results = model(preds)
# results.render()
# df = results.pandas().xyxy[0]
# df1 = pd.DataFrame(df)
#df1 = df.drop(['confidence','class'], axis=1)
#print(df1)
print("hello")
#list_label = []
#list_images = []

# for index in range(0,len(df1)):
#     information['name']+= [labels[index]]
#     information['label']+= [df1['name'][index]]
#     information['xmin']+= [df1['xmin'][index]]
#     information['xmax']+= [df1['xmax'][index]]
#     information['ymin']+= [df1['ymin'][index]]
#     information['ymax']+= [df1['ymax'][index]]
#     information['image']+= [f'{origpred}/{labels[index]}']

# for index,im in enumerate(results.imgs):
#     img = Image.fromarray(im)
#     #img.save(f'{predict_path}/{labels[index]}')
    
#     img.save(f'{origpred}/{labels[index]}')

annots_data = pd.DataFrame(information)
annots_data.to_pickle(os.path.join(pred_path,'v{}.pkl'.format(params['count'])))
print(annots_data)
