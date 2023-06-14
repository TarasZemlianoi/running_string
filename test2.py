#_*_ coding: utf-8 -*-
import cv2
import numpy as np
import pygame


pygame.init()

# параметры видеоизображения
framesize = 100
movie_time = 3
fps = 30
font_size = 15
myfont = pygame.font.SysFont('times', font_size, bold=False, italic=False)
frames_qty = movie_time * fps


input_text =  input('Введите тексст для бегущей строки: ')
mytext = myfont.render(input_text, False, (255,255,255))

txt_np = pygame.surfarray.array3d(mytext)
txt_np = txt_np.transpose((1,0,2))

txt_length = mytext.get_size()[0]
txt_height = mytext.get_size()[1]

out = cv2.VideoWriter('priv.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (framesize, framesize))
#out = cv2.VideoWriter('priv.mp4', cv2.VideoWriter_fourcc(*'MP4V'), fps, (framesize, framesize))

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
    out.write(img)
out.release()