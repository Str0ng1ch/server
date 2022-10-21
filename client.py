import socket
import config
from threading import Thread


def connection(sock, address, port):
    sock.connect((address, port))
    print('Произошло соединение с сервером')


def send_data(sock):
    while True:
        data = input()
        sock.send(data.encode())
        print(f'Отправлены данные: {data}')


def receive_data(sock):
    while True:
        data = sock.recv(2048)
        msg = data.decode()
        print(f'Получено сообщение: {msg}')


def end_session(sock):
    sock.close()
    print(f'Соединение с сервером разорвано')


def main():
    sock = socket.socket()
    address, port = 'localhost', config.port
    connection(sock, address, port)
    sock.send(config.msg.encode())
    print(f'Отправлено сообщение {config.msg}')
    t1 = Thread(target=receive_data(sock))
    t2 = Thread(target=send_data(sock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


main()
