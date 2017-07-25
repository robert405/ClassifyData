from PIL import Image
import numpy as np

def load_image(infilename) :
    img = Image.open(infilename)
    img.load()
    wsize = (int)(float(img.size[0]) / 2)
    hsize = (int)(float(img.size[1]) / 2)
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    data = np.asarray(img, dtype="int32" )
    return data

def save_image(filename, data):
    data = data.astype('uint8')
    im = Image.fromarray(data)
    im.save(filename)

def removeMean(img):

    mean = np.mean(img)

    return (img - mean)