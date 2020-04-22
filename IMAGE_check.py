import os
import re
import cv2
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

x_total = np.load("x_total_110_164_9_6.npy")
for i in range(50):
    imshow(x_total[i])
    plt.show()