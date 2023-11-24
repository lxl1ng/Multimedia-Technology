from PIL import Image, ImageTk


def resize(w, h, pil_image):
    f1 = 1.0 * 250 / w
    f2 = 1.0 * 250 / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


resize(600,400)