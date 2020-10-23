import socket
import json
import sys

SEARCH_NAME = 'search_name'
SEARCH_CONTENT = 'search_content'
DOWNLOAD = 'download'
UPLOAD = 'upload'
LOGIN = 'login'
LOGOUT = 'logout'

token = ''

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    if msg == LOGIN:
        username = input('Digite o username: ')
        password = input('Digite o password: ')
        data = {"success": "true", "status": 200, "message": msg, LOGIN: [username, password]}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    elif msg == LOGOUT:
        data = {"success": "true", "status": 200, "message": msg, "token": token}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    elif msg == 'list':
        data = {"success": "true", "status": 200, "message": msg, "token": token}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    elif msg == SEARCH_NAME:
        searcher = input("Qual arquivo buscar ")
        data = {"success": "true", "status": 200, "message": msg, SEARCH_NAME: searcher, "token": token}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    elif msg == SEARCH_CONTENT:
        searcher = input("Qual conteudo buscar ")
        data = {"success": "true", "status": 200, "message": msg, SEARCH_CONTENT: searcher, "token": token}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    elif msg == UPLOAD:
        file_name = input("Digite o nome do arquivo ")
        file_content = input("Qual conteudo do arquivo ")
        file = [file_name, file_content]
        data = {"success": "true", "status": 200, "message": msg, UPLOAD: file, "token": token}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    elif msg == DOWNLOAD:
        file_name = input("Digite o nome do arquivo ")
        file_content = input("Qual conteudo do arquivo ")
        file = [file_name, file_content]
        data = {"success": "true", "status": 200, "message": msg, DOWNLOAD: file, "token": token}
        request = json.dumps(data)
        tcp.sendall(bytes(request, encoding='utf-8'))
    

    msg = tcp.recv(1024)
    # print(cliente, msg)
    request = json.loads(msg)
    status = request['status']
    operation = request['message']
    if status == 202:
        token = request['message']
    print(operation)
    msg = input()
tcp.close()