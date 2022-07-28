import torch
import sys
import os
from PIL import Image
import yaml
import pandas as pd
import glob
import xml.etree.ElementTree as ET


params = yaml.safe_load(open('params.yaml'))['prepare']
images = os.path.join('data','prepared',f"v{params['count']}",'images')

annots = os.path.join('data','prepared',f"v{params['count']}",'annotations')
transformed_data_path = os.path.join('data','transformed','v{}'.format(params['count']))

os.makedirs(transformed_data_path,exist_ok=True)

def generate_data( Annotpath, Imagepath):
		information={'xmin':[],'ymin':[],'xmax':[],'ymax':[],'ymax':[],'name':[] ,'label':[], 'image':[]}
		for file in sorted(glob.glob(str(Annotpath+'/*.xml*'))):
			dat=ET.parse(file)
			for element in dat.iter():    
				if 'object'==element.tag:
					for attribute in list(element):
						if 'name' in attribute.tag:
							name = attribute.text
							file_name = file.split('/')[-1][0:-4]
							information['label'] += [name]
							information['name'] +=[file_name]
							#information['name'] +=[file]
							information['image'] += [os.path.join(Imagepath, file_name + '.jpg')]
						if 'bndbox'==attribute.tag:
							for dim in list(attribute):
								if 'xmin'==dim.tag:
									xmin=int(round(float(dim.text)))
									information['xmin']+=[xmin]
								if 'ymin'==dim.tag:
									ymin=int(round(float(dim.text)))
									information['ymin']+=[ymin]
								if 'xmax'==dim.tag:
									xmax=int(round(float(dim.text)))
									information['xmax']+=[xmax]
								if 'ymax'==dim.tag:
									ymax=int(round(float(dim.text)))
									information['ymax']+=[ymax]
		return pd.DataFrame(information)



df = generate_data(annots,images)
df.to_pickle(os.path.join(transformed_data_path,'v{}.pkl'.format(params['count'])))
print(df)

