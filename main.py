# -*- coding: utf-8 -*-
import socket
import time
import picamera
import subprocess
import random
import RPi.GPIO as GPIO
import subprocess

# Juliusに接続する準備///////////////////////////////////////////////
subprocess.run('julius -C ~/lumos/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/lumos/julius/dict/lumos -input mic -module')
host = 'localhost'
port = 10500
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
res = ''
# Juliusに接続する準備///////////////////////////////////////////////

# LEDの準備/////////////////////////////////////////////////////////
led_state = 0

# LEDピンの設定
led_pin = 24
# BOARD: ピン番号で指定するモード
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
# PWMの設定
Led = GPIO.PWM(led_pin, 50)
# 初期化処理
Led.start(0)  # PWM信号0%出力
bright = 0  # デューティー比で明るさを決める変数"bright"に0を代入
# LEDの準備/////////////////////////////////////////////////////////


# このループ処理は常に回っている
while True:
    # 音声認識の区切りである「改行+.」が来たときのみこのループが回らず、次に移行する///////////////////
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
            line = line[index + 6: line.find('"', index + 6)]
            # 文字列の開始記号以外を格納していく
            if line != '[s]':
                word = word + line
                print('word：' + word)
                # オフなら消灯、ルーモスなら弱点灯、ルーモスマキシマなら強点灯のステートに更新する
                if word == "おふ":
                    led_state = 0
                elif word == "るうもす":
                    led_state = 1
                elif word == "るうもすまきしま":
                    led_state = 2
        res = ''
    # 音声認識の区切りである「改行+.」が来たときのみこのループが回る/////////////////////

    # Stateに合わせてLED点灯させる
    try:
        Led.ChangeDutyCycle(bright)  # PWM信号出力(デューティ比は変数"bright")
        time.sleep(0.05)  # 0.05秒間待つ
        bright = state*50  # duty比は0~100で、0のとき消灯、100のとき最大照度

    except KeyboardInterrupt:  # Ctrl+Cキーが押された
        Led.stop()  # LED点灯をストップ
        GPIO.cleanup()  # GPIOをクリーンアップ
        sys.exit()  # プログラムを終了