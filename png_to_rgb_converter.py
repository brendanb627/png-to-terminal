
def png_to_rgb(img_path):
    from PIL import Image
    img = Image.open(img_path)
    return list(img.getdata())
        
