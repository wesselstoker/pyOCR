from werkzeug import secure_filename
from pytesser import *
import Image
import os

upload_dir = 'images/uploads/'
allowed_images = set(['png', 'jpg'])

def construct(file):
    if file and checkImage(file.filename):
        file_path = uploadImage(file)
        convertImage(file,file_path)
        return callOcr()
    else:
        return "Only .png, .jpg and jpeg are allowed."

def checkImage(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_images

def uploadImage(file):
    file_path = upload_dir + secure_filename(file.filename)
    file.save(file_path)
    return file_path

def convertImage(file,file_path):
    if file.content_type == "image/jpg":
        Image.open(file_path).save("images/temp.bmp", "BMP")
        Image.open('images/temp.bmp').convert('L').save('images/temp.bmp')
    
    elif file.content_type == "image/jpeg":
        Image.open(file_path).save("images/temp.bmp", "BMP")
        Image.open('images/temp.bmp').convert('L').save('images/temp.bmp')

    elif file.content_type == "image/png":    
        img = Image.open(file_path)
        if img.mode == "RGB":
            r, g, b = img.split()
        elif img.mode == "RGBA":
            r, g, b,a = img.split()
        else:
            print "[error] image mode is:" + img.mode 
            print "[error] image mode isnt RGB or RGBA."
        
        img = Image.merge("RGB", (r, g, b))
        img.save("images/temp.bmp")
        Image.open('images/temp.bmp').convert('L').save('images/temp.bmp')
    else:
        print "[error] Failed to convert Image" 

def callOcr():
        return image_to_string(Image.open('images/temp.bmp'))
