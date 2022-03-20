led_state = 0

while True:
    word = input()

    if word == "おふ":
        led_state = 0
    elif word == "るうもす":
        led_state = 1
    elif word == "るうもすまきしま":
        led_state = 2
        
    print(led_state)