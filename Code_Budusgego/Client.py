import socket

def run_server():
    # Создание серверного сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязка сокета к локальному адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Ожидание соединения
    server_socket.listen(1)
    print("Сервер запущен. Ожидание подключения клиента...")

    # Принятие подключения от клиента
    client_socket, client_address = server_socket.accept()
    print("Клиент подключен. Рабочий сокет создан.")

    # Чтение данных от клиента и отправка их обратно
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)

    # Закрытие сокетов
    client_socket.close()
    server_socket.close()

def run_client():
    # Создание клиентского сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение к серверу
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    print("Соединение установлено. Рабочий сокет создан.")

    # Ввод и отправка данных серверу
    while True:
        message = input("Введите сообщение: ")
        client_socket.sendall(message.encode())

        # Получение и вывод ответа от сервера
        data = client_socket.recv(1024)
        print("Ответ сервера:", data.decode())

        # Выход из цикла по условию
        if message.lower() == 'exit':
            break

    # Закрытие сокета
    client_socket.close()

def main():
    choice = input("Выберите режим работы (s - сервер, c - клиент): ")
  
    if choice.lower() == 's':
        run_server()
    elif choice.lower() == 'c':
        run_client()

if __name__ == '__main__':
    main()
