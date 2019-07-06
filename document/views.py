from django.shortcuts import render,redirect
from django.http import HttpResponse
import pytesseract
from PIL import Image
import numpy as np
import random
import math
from django.core.files.storage import FileSystemStorage
import os,glob


def uplaod(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        x = math.ceil(np.random.rand() * 10000)
        result = f'result{x}.txt'
        image = Image.open(f'C:/Users/r12/PycharmProjects/index/venv/Scripts/upload/media/{uploaded_file.name}')
        text = pytesseract.image_to_string(image, lang='eng')

        media_files = glob.glob('C:/Users/r12/PycharmProjects/index/venv/Scripts/upload/media/*')
        for file in media_files:
            os.remove(file)


        with open(result, 'w', encoding="utf-8") as file:
            file.write(text)
        with open(result, 'r') as file:
            lines = file.readlines()
            print(lines)
            # line_3 = lines[3].replace('â€”', '-')
            # line_4 = lines[4]
            # line_5 = lines[5]
            # line_7 = lines[7]
            # line_8 = lines[8].replace('â€”', '-')
            # line_18 = lines[18]
            # return render(request, 'document/result.html', {'line_3': line_3, 'line_4': line_4, 'line_5': line_5,
            #                                                 'line_7' : line_7, 'line_8': line_8, 'line_18': line_18})
            return render(request, 'document/result.html',{'lines':lines})
    return render(request, 'document/upload.html')


