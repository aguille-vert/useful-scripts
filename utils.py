import numpy as np
from io import Bytes io
import matplotlib.pyplot as plt

def preview_images(images, titles, n, n_cols,figsize=(12, 8)):
    """
    Shows multiple images arranged in rows and columns in a single matplotlib chart
    Params:
    =======
        images (list): list of images as np arrays dtype='uint8' HxWxC
        titles (list): list of str, will be shown as title of each image in chart
        n (int): number of images to visualize; n and cols determine number of rows
        n_cols (int): number of columns which images will be arranged by
        figsize (tuple): size of matplotlib chart
    """
    sample_images = images[:n]
    sample_labels = titles[:n]

    rows = int(np.ceil(n / n_cols))
    fig, axs = plt.subplots(rows, n_cols, figsize=figsize)

    for i, ax in enumerate(axs.flatten()):
        image = sample_images[i]
        label = sample_labels[i]
        ax.imshow(image)
        ax.axis("off")
        ax.set_title(f"Label: {label}")

    plt.tight_layout()
