import cv2
import os
from PIL import Image
import time
import sys
from pydub import AudioSegment
import subprocess

# 字符集，根据亮度从高到低排序
ASCII_CHARS = '@%#*+=-:.'

def resize_image(image, new_width=200):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def image_to_ascii(image: Image):
    pixels = image.getdata()
    ascii_str = ''
    for idx, pixel in enumerate(pixels):
        # 将 RGB 值转换为亮度值
        brightness = sum(pixel) // 3
        # 根据亮度值映射到字符集
        ascii_str += ASCII_CHARS[brightness * (len(ASCII_CHARS) - 1) // 255]
    return ascii_str

def convert_frames_to_ascii(video_path, frame_interval, width):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    success = True

    while success:
        success, frame = video.read()

        # 按指定的间隔抽取帧
        if frame_count % frame_interval == 0:

            # 将帧转换为 PIL 图像
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            # 调整图像大小
            resized_image = resize_image(image, width)
            # 将图像转换为字符画
            ascii_str = image_to_ascii(resized_image)
            time.sleep(1/30*(0.19))
            os.system("clear")
            # 输出字符画到终端
            for i in range(len(ascii_str) //width):
                print(ascii_str[i*width:(i+1)*width])


        frame_count += 1

    video.release()

def play_audio(audio_path):
    # 播放音频
    subprocess.Popen(['ffplay', '-nodisp', '-autoexit', audio_path])


if __name__ == "__main__":

    video_path = "./video/badapple.mp4"  # 输入视频文件路径
    frame_interval = 1  # 抽帧间隔，每隔30帧抽取一帧
    width = 245
    play_audio(video_path)
    convert_frames_to_ascii(video_path, frame_interval, width)
