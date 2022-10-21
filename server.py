import socket
import config
import threading


class ClientThread(threading.Thread):
    def __init__(self, address, socket):
        threading.Thread.__init__(self)
        self.client_socket = socket
        print(f'Подключение по адрессу: {address}')

    def run(self):
        while True:
            data = self.client_socket.recv(2048)
            msg = data.decode()
            print(msg)
            if msg == "":
                break
            else:
                print(f'Получено сообщение {msg}')
                self.client_socket.send(msg.encode())
                print(f'Отправлено сообщение {msg}')



def port_listening(sock):
    address, port = '', config.port
    sock.bind((address, port))
    sock.listen(1)
    print(f'Началось прослушивание порта {port}')


def end_session(conn):
    conn.close()
    print('Отключение клиента')


def stop(sock):
    sock.close()
    print('Остановка сервера')


def main():
    sock = socket.socket()
    print('Сервер запустился')
    port_listening(sock)
    while True:
        conn, addr = sock.accept()
        newthread = ClientThread(addr, conn)
        newthread.start()


main()
 
