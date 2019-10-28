import cv2
import os

def _compress_image(file_path, quality):
    """ A method that compress an image from given path, then overwrite the image.

    Args:
        file_path: The path of the image. Supported formats includes jpeg, jpg, png.
            The file will be overwritten by the compressed image.
        quality: The quality of the compressed image. From 0 to 100, the bigger 
            `quality` is, the better quality the image is.
    """
    if quality >= 100:
        return
    image = cv2.imread(file_path)
    os.remove(file_path)
    cv2.imwrite(file_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
