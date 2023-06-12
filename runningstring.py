from moviepy.editor import TextClip
from moviepy.editor import *
# для работы скрипта необходимо установить ImageMagick

# Введите текст
your_text = input("Введите текст для бегущей строки: ")

# параметры бегущей строки
clip_size = 100
dur = 3
fnt_size = 20

# создаем текстовый клип
txt_clip = TextClip(your_text, color='white', align='West',fontsize=fnt_size,
                    font='Courier', method='label')

# рассчитываем скорость движения текста
txt_length = txt_clip.size[0]
txt_speed = (clip_size + txt_length) / dur

moving_clip = txt_clip.set_position(lambda t: (int(clip_size - txt_speed*t), 'center'))

# Создание видеоклипа с черным фоном
background = ColorClip((100, 100), color=(20, 50,100)).set_duration(dur)
final = CompositeVideoClip([background, moving_clip])
# Сохранение видео в файл
final.set_duration(dur).write_videofile(your_text + '.mp4', fps=60, codec='libx264')

