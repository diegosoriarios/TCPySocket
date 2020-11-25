import socket
import json
import random
import os
from utils import SEARCH_NAME, SEARCH_CONTENT, DOWNLOAD, UPLOAD, LOGIN, LOGOUT, LIST
from utils import STATE, MESSAGES, STATUS
STATE = STATE()
MESSAGES = MESSAGES()
STATUS = STATUS()

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

class Candidatos:
    def __init__(self, nome, numero, partido):
        self.nome = nome
        self.numero = numero
        self.partido = partido
    
    def vote(self):
        self.numero = self.numero + 1

candidatos = [
    Candidatos('Diego', 2, 'Lazy'),
    Candidatos('Daniel', 1, 'Study')
]

votacao = {
    "candidatos": candidatos,
    "status": True,
}

users = [
    ['elder', '123456', False],
    ['diego', 'senha', False],
    ['teste', 'teste', False],
]

SEARCH_NAME = 'search_name'
SEARCH_CONTENT = 'search_content'
DOWNLOAD = 'download'
UPLOAD = 'upload'
LOGIN = 'login'
LOGOUT = 'logout'

while True:
    con, cliente = tcp.accept()
    
    pid = os.fork()

    if pid == 0:
        tcp.close()
        print('Concetado por', cliente)
        state = STATE.CONNECTED

        while True:
            msg = con.recv(1024)
            if not msg: break
            # print(cliente, msg)
            request = json.loads(msg)
            operation = request['operation']
            print(cliente, operation)

            if state == STATE.CONNECTED:
                if operation == MESSAGES.LOGIN:
                    token = ""
                    client = request['client']
                    password = request['password']
                    flag = False
                    for user in users:
                        if client.lower() in user[0]:
                            if password.lower() in user[1]:
                                flag = True
                                if user[2]:
                                    state = STATE.ADMIN
                                    data = {"operation": MESSAGES.ADMINLOGINREPLY, "response": "Bem vindo " + client, "status": STATUS.OK}
                                    request = json.dumps(data)
                                    con.sendall(bytes(request, encoding='utf-8'))
                                else:
                                    state = STATE.AUTHENTICATED
                                    data = {"operation": MESSAGES.LOGINREPLY, "response": "Bem vindo " + client, "status": STATUS.OK}
                                    request = json.dumps(data)
                                    con.sendall(bytes(request, encoding='utf-8'))
                    if flag:
                        data = {"operation": MESSAGES.LOGINREPLY, "response": "Client ou Senha não encontrados", "status": STATUS.ERROR}
                        request = json.dumps(data)
                        con.sendall(bytes(request, encoding='utf-8'))
                else:
                    data = {"operation": MESSAGES.LOGINREPLY, "response": "É preciso estar logado", "status": STATUS.ERROR}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
            elif state == STATE.AUTHENTICATED:
                if operation == MESSAGES.LOGOUT:
                    state = STATE.CONNECTED
                    data = {"operation": MESSAGES.LOGOUTREPLY, "response": "Volte sempre", "status": STATUS.OK}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
                elif operation == MESSAGES.VOTE:
                    numero = request['vote']
                    flag = False
                    for candidato in votacao['candidatos']:
                        if candidato.numero == numero:
                            flag = True
                            candidato.vote()
                    if flag:
                        data = {"operation": MESSAGES.VOTEREPLY, "response": "Voto computado, muito obrigado", "status": STATUS.OK}
                        request = json.dumps(data)
                        con.sendall(bytes(request, encoding='utf-8'))
                    else:
                        data = {"operation": MESSAGES.VOTEREPLY, "response": "Candidato não encontrado", "status": STATUS.ERROR}
                        request = json.dumps(data)
                        con.sendall(bytes(request, encoding='utf-8'))
                elif operation == MESSAGES.LISTCANDIDATOS:
                    list_candidatos = []
                    for candidato in votacao['candidatos']:
                        list_item = [candidato.nome, candidato.numero]
                        list_candidatos.append(list_item)
                    data = {"operation": MESSAGES.LISTCANDIDATOSREPLY, "response": list_candidatos, "status": STATUS.OK}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
                elif operation == MESSAGES.CONSULTRESULT:
                    if votacao['status']:
                        data = {"operation": MESSAGES.CONSULTRESULTREPLY, "response": "A votação está em andamento", "status": STATUS.ERROR}
                        request = json.dumps(data)
                        con.sendall(bytes(request, encoding='utf-8'))
                    else:
                        data = {"operation": MESSAGES.CONSULTRESULTREPLY, "response": votacao['candidatos'], "status": STATUS.OK}
                        request = json.dumps(data)
                        con.sendall(bytes(request, encoding='utf-8'))
            elif state == STATE.ADMIN:
                if operation == MESSAGES.ADDCANDIDATO:
                    nome = request['nome']
                    numero = request['numero']
                    partido = request['partido']
                    novo_candidato = Candidatos(nome, numero, partido)
                    votacao['candidatos'].append(novo_candidato)
                    data = {"operation": MESSAGES.ADDCANDIDATOREPLY, "response": "Candidato adicionado", "status": STATUS.OK}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
                elif operation == MESSAGES.STARTVOTE:
                    votacao['status'] = True
                    data = {"operation": MESSAGES.STARTVOTEREPLY, "response": "Votação Iniciada", "status": STATUS.OK}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
                elif operation == MESSAGES.ENDVOTE:
                    votacao['status'] = False
                    data = {"operation": MESSAGES.ENDVOTEREPLY, "response": "Votação encerrada", "status": STATUS.OK}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
                elif operation == MESSAGES.LOGOUT:
                    data = {"operation": MESSAGES.LOGOUTREPLY, "response": "Volte Sempre", "status": STATUS.OK}
                    request = json.dumps(data)
                    con.sendall(bytes(request, encoding='utf-8'))
            else:
                data = {"status": 401, "message": "Unauthorized", "operation": "Error_reply"}
                request = json.dumps(data)
                con.sendall(bytes(request, encoding='utf-8'))

        print('Finalizando conexao do cliente', cliente)
        con.close()
    else:
        con.close()