import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.colors import LogNorm

def plot_image(image, normalized = True, Save = False, outpath = "./", title = "Image"):
    plt.figure(figsize=(15,15))
    plt.imshow(image, origin='lower',norm=LogNorm(vmin=0.01))
    plt.colorbar()
    plt.xlabel("η", fontsize=20)
    plt.ylabel("Φ", fontsize=20)
    plt.title(title, fontsize=20)
    if Save:
        plt.savefig(outpath+"event.pdf")
    else:
        plt.show()
        
def plot_images(image_vector, normalized = False, Save = False, outpath = "./", title = "Image"):

    for num, image in enumerate(image_vector):
        plt.figure(figsize=(15,15))
        plt.imshow(image, origin='lower',norm=LogNorm(vmin=0.01))
        plt.colorbar()
        plt.xlabel("η", fontsize=20)
        plt.ylabel("Φ", fontsize=20)
        plt.title(title, fontsize=20)
        if Save:
            plt.savefig(outpath+"/event_{}.pdf".format(num))
        else:
            plt.show()