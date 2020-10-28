import socket
import json
import sys
from utils import SEARCH_NAME, SEARCH_CONTENT, DOWNLOAD, UPLOAD, LOGIN, LOGOUT, LIST

token = ''

def send_message(data, tcp):
    request = json.dumps(data)
    tcp.sendall(bytes(request, encoding='utf-8'))

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
error = False
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    error = False
    if msg == LOGIN:
        username = input('Digite o username: ')
        password = input('Digite o password: ')
        data = {"status": 200, "message": msg, LOGIN: [username, password]}
        send_message(data, tcp)
    elif msg == LOGOUT:
        data = {"status": 200, "message": msg, "token": token}
        send_message(data, tcp)
    elif msg == LIST:
        data = {"status": 200, "message": msg, "token": token}
        send_message(data, tcp)
    elif msg == SEARCH_NAME:
        searcher = input("Qual arquivo buscar ")
        data = {"status": 200, "message": msg, SEARCH_NAME: searcher, "token": token}
        send_message(data, tcp)
    elif msg == SEARCH_CONTENT:
        searcher = input("Qual conteudo buscar ")
        data = {"status": 200, "message": msg, SEARCH_CONTENT: searcher, "token": token}
        send_message(data, tcp)
    elif msg == UPLOAD:
        file_name = input("Digite o nome do arquivo ")
        file_content = input("Qual conteudo do arquivo ")
        file = [file_name, file_content]
        data = {"status": 200, "message": msg, UPLOAD: file, "token": token}
        send_message(data, tcp)
    elif msg == DOWNLOAD:
        file_name = input("Digite o nome do arquivo ")
        file_content = input("Qual conteudo do arquivo ")
        file = [file_name, file_content]
        data = {"status": 200, "message": msg, DOWNLOAD: file, "token": token}
        send_message(data, tcp)
    else:
        error = True
        print("Comando não reconhecido")
    

    if error == False:
        msg = tcp.recv(1024)
        # print(cliente, msg)
        request = json.loads(msg)
        status = request['status']
        operation = request['operation']
        response = request['message']
        if status == 202:
            token = request['message']
        print(operation, response)
    msg = input()
tcp.close()