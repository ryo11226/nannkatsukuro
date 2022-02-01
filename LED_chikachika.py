import RPi.GPIO as GPIO
import time

def ledadjust(state):

    # LEDピンの設定
    led_pin = 24

    # BOARD: ピン番号で指定するモード
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)

    # PWMの設定
    Led = GPIO.PWM(led_pin, 50)

    #初期化処理
    Led.start(0)     #PWM信号0%出力
    bright = 0       #変数"bright"に0を代入

    # ループ処理
    # LEDの明るさをstateに合わせて変更
    while True:
        try:
            Led.ChangeDutyCycle(bright)    #PWM信号出力(デューティ比は変数"bright")
            time.sleep(0.05)               #0.05秒間待つ
            bright = state*50              #duty比は0~100で、0のとき消灯、100のとき最大照度
                
        except KeyboardInterrupt:          #Ctrl+Cキーが押された
            Led.stop()                     #LED点灯をストップ
            GPIO.cleanup()                 #GPIOをクリーンアップ
            sys.exit()                     #プログラムを終了