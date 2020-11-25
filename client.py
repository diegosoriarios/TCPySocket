import socket
import json
import sys
from utils import SEARCH_NAME, SEARCH_CONTENT, DOWNLOAD, UPLOAD, LOGIN, LOGOUT, LIST
from utils import MESSAGES, STATUS, STATE

token = ''

def send_message(data, tcp):
    request = json.dumps(data)
    tcp.sendall(bytes(request, encoding='utf-8'))

def print_options():
    if token:
        print('-------------------------------')
        print('| logout             list     |')
        print('| search_name        upload   |')
        print('| search_content     download |')
        print('-------------------------------')
    else:
        print('-------------------------------')
        print('|                             |')
        print('|            login            |')
        print('|                             |')
        print('-------------------------------')

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
error = False
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
print_options()
msg = input()
while msg != '\x18':
    error = False
    if msg == LOGIN:
        client = input('Digite o client: ')
        password = input('Digite o password: ')
        data = {"client": client, "password": password, "operation": MESSAGES.LOGIN}
        send_message(data, tcp)
    elif msg == LOGOUT:
        data = {"operation": MESSAGES.LOGOUT}
        send_message(data, tcp)
    elif msg == 'start_vote':
        data = {"operation": MESSAGES.STARTVOTE}
        send_message(data, tcp)
    elif msg == 'add_candidato':
        candidato = input("Qual o nome do candidato? ")
        numero = input("Qual o numero do candidato? ")
        partido= input("Qual o partido do candidato? ")
        data = {"operation": MESSAGES.ADDCANDIDATO, "nome": candidato, "numero": numero, "partido": partido}
        send_message(data, tcp)
    elif msg == 'list_candidatos':
        data = {"operation": MESSAGES.LISTCANDIDATOS}
        send_message(data, tcp)
    elif msg == 'end_vote':
        data = {"operation": MESSAGES.ENDVOTE}
        send_message(data, tcp)
    elif msg == 'consult_result':
        data = {"operation": MESSAGES.CONSULTRESULT}
        send_message(data, tcp)
    elif msg == 'vote':
        numero = input("Qual o numero? ")
        data = {"operation": MESSAGES.VOTE, "numero": numero}
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
    print_options()
    msg = input()
tcp.close()