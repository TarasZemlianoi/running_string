from moviepy.editor import *
import numpy as np
import pygame

pygame.init()

# параметры видеоизображения
framesize = 100
movie_time = 3
fps = 30
font_size = 15
myfont = pygame.font.SysFont('Times', font_size, bold=False, italic=False)
frames_qty = movie_time * fps

# ввод текста
input_text =  input('Введите текст для бегущей строки: ')
mytext = myfont.render(input_text, False, (255,255,255))

#преобразование изображение текста в numpy array
txt_np = pygame.surfarray.array3d(mytext)
txt_np = txt_np.transpose((1,0,2))

# размеры, проходимый путь, покадровое смещение, координаты бегущей строки
txt_length = mytext.get_size()[0]
txt_height = mytext.get_size()[1]
txt_move_size = framesize + txt_length
frame_step = txt_move_size/frames_qty
txt_x = 0
txt_y = (framesize - txt_height)//2

# массив кадров
img_array = []

for _ in range(0, frames_qty):
  txt_x += frame_step
  img = np.zeros((framesize, framesize, 3), dtype = np.uint8)
  txt_np_slice = txt_np[:,abs(np.minimum(0, framesize - round(txt_x))): np.minimum(txt_length, round(txt_x))].copy()
  img[txt_y:txt_y+len(txt_np_slice),
    np.maximum(0, framesize-round(txt_x)): np.maximum(0, framesize-round(txt_x)) + len(txt_np_slice[0])] = txt_np_slice
  img_array.append(img)

clip = ImageSequenceClip(img_array, fps=fps, durations=movie_time)
# clip = ImageClip(img, 0, 1, 0, 3)

# clip.set_duration(3)
# clip.fps = 24
clip.write_videofile('strangename.mp4')