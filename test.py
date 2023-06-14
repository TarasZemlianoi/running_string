#_*_ coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image,ImageFont,ImageDraw
import os

# параметры видеоизображения
framesize = 100
movie_time = 3
fps = 60
font_size = 20
frames_qty = movie_time * fps

print(os.path.join("fonts", "arial.ttf"))
#вводим текст для отображения
my_text = input('Введите тексст для бегущей строки: ')

fnt = ImageFont.truetype(os.path.join("fonts", "arial.ttf"), font_size)

# находим размер текста в пикселях и преобразуем текст в изоображение
txt_box = fnt.getbbox(my_text)
txt_length = txt_box[2]
txt_height = txt_box[3]
print(txt_length, txt_height)
print(txt_box)
im = Image.new(mode='RGB', size=(txt_length, txt_height))
dr = ImageDraw.Draw(im)
dr.text((0, 0), my_text, font=fnt, fill=(255,255,255))

txt_np = np.array(im)

out = cv2.VideoWriter('priv.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (framesize, framesize))
# out = cv2.VideoWriter('priv', cv2.VideoWriter_fourcc(*'MPEG'), 30, framesize)

txt_move_size = framesize + txt_length
frame_step = txt_move_size/frames_qty
txt_x = 0
txt_y = (framesize - txt_height)//2
for _ in range(0, frames_qty):
    txt_x += frame_step
    img = np.zeros((100, 100, 3), dtype = np.uint8)
    txt_np_slice = txt_np[:,abs(np.minimum(0, framesize - round(txt_x))): np.minimum(txt_length, round(txt_x))].copy()

    img[txt_y:txt_y+len(txt_np_slice),
    np.maximum(0, framesize-round(txt_x)): np.maximum(0, framesize-round(txt_x)) + len(txt_np_slice[0])] = txt_np_slice
    #np.copyto(img, txt_np_slice)
    out.write(img)
out.release()

im.save("priv.png")