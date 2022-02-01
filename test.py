# -*- coding: utf-8 -*-
import socket
import time
import picamera
import subprocess
import random
import LED_chikachika

host = 'localhost'
port = 10500

# Juliusに接続する準備
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

res = ''
led_state = 0

# 音声入力待ちループ処理
while True:
    # 音声認識の区切りである「改行+.」がくるまで待つ
    while (res.find('\n.') == -1):
        # 改行があるまでJuliusから取得した値を格納していく
        res += sock.recv(1024).decode()

    word = ''
    for line in res.split('\n'):
        # Juliusから取得した値から認識文字列の開始位置を探す
        index = line.find('WORD=')
        # 認識文字列があったら...
        if index != -1:
            # 認識文字列部分だけを抜き取る、WORD=" で6文字使用するので7文字目から
            line = line[index + 6 : line.find('"', index + 6)]
            # 文字列の開始記号以外を格納していく
            if line != '[s]':
                word = word + line
                print('word：' + word)
                # オフなら消灯、ルーモスなら弱点灯、ルーモスマキシマなら強点灯
                if word == "おふ":
                    led_state = 0
                elif word == "るうもす":
                    led_state = 1
                elif word == "るうもすまきしま":
                    led_state = 2 
        res = ''

# LED点灯
LED_chikachika.ledadjust(state)