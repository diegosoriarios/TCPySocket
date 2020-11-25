import socket
import json
import sys
from utils import SEARCH_NAME, SEARCH_CONTENT, DOWNLOAD, UPLOAD, LOGIN, LOGOUT, LIST
from utils import MESSAGES, STATUS, STATE

MESSAGES = MESSAGES()
STATUS = STATUS()
STATE = STATE()

state = STATE.CONNECTED

def send_message(data, tcp):
    request = json.dumps(data)
    tcp.sendall(bytes(request, encoding='utf-8'))

def print_options():
    if state == STATE.AUTHENTICATED:
        print('--------------------------------------')
        print('| logout              vote           |')
        print('| list_candidatos     consult_result |')
        print('--------------------------------------')
    elif state == STATE.ADMIN:
        print('---------------------------------')
        print('| add_candidato      start_vote |')
        print('| end_vote           logout     |')
        print('---------------------------------')
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
    print(msg)
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
        operation = request['operation']
        if operation == MESSAGES.LOGINREPLY:
            status = request['status']
            if status == STATUS.OK:
                state = STATE.AUTHENTICATED
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.ADMINLOGINREPLY:
            status = request['status']
            if status == STATUS.OK:
                state = STATE.ADMIN
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.LOGOUTREPLY:
            status = request['status']
            if status == STATUS.OK:
                state = STATE.EXIT
            state = STATE.EXIT
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.STARTVOTEREPLY:
            state = STATE.AUTHENTICATED
            status = request['status']
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.ADDCANDIDATOREPLY:
            state = STATE.AUTHENTICATED
            status = request['status']
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.LISTCANDIDATOSREPLY:
            state = STATE.AUTHENTICATED
            status = request['status']
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.ENDVOTEREPLY:
            state = STATE.AUTHENTICATED
            status = request['status']
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.CONSULTRESULTREPLY:
            state = STATE.AUTHENTICATED
            status = request['status']
            response = request['response']
            print(operation, response)
        elif operation == MESSAGES.VOTEREPLY:
            state = STATE.AUTHENTICATED
            status = request['status']
            response = request['response']
            print(operation, response)
    print_options()
    msg = input()
tcp.close()