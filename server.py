import socket
import json
import random

HOST = ''
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

db = [
    ["Green day", "American Idiot"],
    ["Green day", "Jesus Of Suburbia"],
    ["Green day", "Holiday"],
]

users = [
    ['elder', '123456'],
    ['diego', 'senha'],
    ['teste', 'teste'],
]

SEARCH_NAME = 'search_name'
SEARCH_CONTENT = 'search_content'
DOWNLOAD = 'download'
UPLOAD = 'upload'
LOGIN = 'login'
LOGOUT = 'logout'

while True:
    con, cliente = tcp.accept()
    print('Concetado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        # print(cliente, msg)
        request = json.loads(msg)
        operation = request['message']
        print(operation)

        if operation == LOGIN:
            token = ""
            username = request[LOGIN][0]
            password = request[LOGIN][1]
            for user in users:
                if username.lower() in user[0]:
                    if password.lower() in user[1]:
                        token = "token"
            data = {"success": "true", "status": 202, "message": token}
            request = json.dumps(data)
            con.sendall(bytes(request, encoding='utf-8'))
        elif request['token']:
            if operation == 'list':
                data = {"success": "true", "status": 200, "message": db}
                request = json.dumps(data)
                con.sendall(bytes(request, encoding='utf-8'))
            elif operation == SEARCH_NAME:
                return_value = []
                search = request[SEARCH_NAME]
                for name in db:
                    if search.lower() in name[0].lower():
                        return_value.append(name)
                
                data = {"success": "true", "status": 200, "message": return_value}
                request = json.dumps(data)
                con.sendall(bytes(request, encoding='utf-8'))
            elif operation == SEARCH_CONTENT:
                return_value = []
                search = request[SEARCH_CONTENT]
                for name in db:
                    if search.lower() in name[1].lower():
                        return_value.append(name)
                
                data = {"success": "true", "status": 200, "message": return_value}
                request = json.dumps(data)
                con.sendall(bytes(request, encoding='utf-8'))
            elif operation == UPLOAD:
                file = request[UPLOAD]
                db.append(file)
                data = {"success": "true", "status": 200, "message": "File Uploaded"}
                request = json.dumps(data)
                con.sendall(bytes(request, encoding='utf-8'))
            elif operation == DOWNLOAD:
                file_name = request[DOWNLOAD][0]
                file_content = request[DOWNLOAD][1]
                
                for name in db:
                    if file_name.lower() in name[0].lower():
                        if file_content.lower() in name[1].lower():
                            data = {"success": "true", "status": 200, "message": name}
                            request = json.dumps(data)
                            con.sendall(bytes(request, encoding='utf-8'))
            elif operation == LOGOUT:
                data = {"success": "true", "status": 202, "message": ""}
                request = json.dumps(data)
                con.sendall(bytes(request, encoding='utf-8'))
        else:
            data = {"success": "false", "status": 401, "message": "Unauthorized"}
            request = json.dumps(data)
            con.sendall(bytes(request, encoding='utf-8'))

    print('Finalizando conexao do cliente', cliente)
    con.close()