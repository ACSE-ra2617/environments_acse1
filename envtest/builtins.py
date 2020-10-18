import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import cv2

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve']


def rand_array(shape):
    return np.random.rand(*shape)


def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)


def my_mat_solve(A, b):
    return A.inv()*b


def create_2_colour_image(height, width):
    blank_image = np.zeros((height, width, 3), np.uint8)
    blank_image[:, 0:width//2] = (255, 0, 0)  # (B, G, R)
    blank_image[:, width//2:width] = (0, 255, 0)
    cv2.imshow('image', blank_image)
    cv2.waitKey(0)
    return blank_image
