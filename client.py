import socket
SERVER_IP = input("ip_address: ")
PORT = 443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, PORT))

while True:
    try:
        message = input(f'{SERVER_IP}>>')
        if message == "quit":
            break
        
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024)
        print(f">>: {response.decode('utf-8')}")
    except:
        pass

client_socket.close()

