from PIL import Image
import numpy as np
import os
import json


def image_convert(file, img_size):

    X = []

    img = Image.open(file)
    img = img.convert('RGB')
    img = img.resize((img_size, img_size))

    in_data = np.asarray(img)

    X.append(in_data)

    X = np.array(X)

    X = X.astype('float') / 256

    return X


# 上位num件の予測結果のkeyを降順で返す
def sort_predict_key(data, num):

    sort_data_key = np.argsort(data)[-1::-1]
    y = sort_data_key[:num]

    return y


def get_plants_name():

    f = open(os.path.join(os.path.dirname(__file__), 'store/plant.json'), 'r')
    json_data = json.load(f)
    categories = list(json_data.values())[0]

    return categories
