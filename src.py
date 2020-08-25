import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters
from skimage.transform import resize, rotate
import pandas as pd

def transform_image(image):
    '''transform images into 1 pixel per row so that they can 
    undergo feature engineeering, aka edge detection '''
    #check if grey or RGB and transform
    if len(image.shape) == 2: #greyscale
        image = np.reshape(image, (-1,1))
    elif len(image.shape) == 3: #rgb
        image = np.reshape(image, (-1,3,1))
    else:
        print(f'This image has a weird shape of {image.shape}')

    print(f'New image shape: {image.shape}')
    return image





if __name__ == "__main__":
    sketch_rgb = io.imread('data/Sketches/ruled/IMG_0006.jpg')
    transform_image(sketch_rgb)