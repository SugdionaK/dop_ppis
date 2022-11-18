class User:
    def __init__(self, name, server):
        self.name = name
        self.server = server
        self.mail = []
        self.server.users.append(self)

    def send(self, to, message):
        if len(message) > 100:
            print("Сообщение слишком длинное")
        else:
            self.server.send(self, to, message)

    def receive(self, message):
        self.mail.append(message)

    def read(self):
        for i in self.mail:
            print(i)


class Server:
    def __init__(self, name):
        self.name = name
        self.users = []

    def send(self, from_, to, message):
        if to in self.users:
            to.receive(message)
        else:
            print("Пользователь не найден")


class Message:
    def __init__(self, from_, to, message):
        self.from_ = from_
        self.to = to
        self.message = message

    def __str__(self):
        return f"from: {self.from_.name}\nto: {self.to.name}\nmessage: {self.message}"


class Client:
    def __init__(self, user):
        self.user = user
        self.user.server = self

    def send(self, to, message):
        self.user.send(to, message)

    def receive(self, message):
        self.user.receive(message)

    def read(self):
        self.user.read()


class MailSystem:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def add_user(self, user):
        self.servers[0].users.append(user)
        user.server = self.servers[0]

    def send(self, from_, to, message):
        if to.server in self.servers:
            to.server.send(from_, to, message)
        else:
            print("Пользователь не найден")


class Controller:
    def __init__(self, mail_system):
        self.mail_system = mail_system

    def send(self, to, message):
        self.client.send(to, message)

    def receive(self, message):
        self.client.receive(message)

    def read(self):
        self.client.read()

    def add_server(self, server):
        self.mail_system.add_server(server)

    def add_user(self, user):
        self.mail_system.add_user(user)

    def send(self, from_, to, message):
        self.mail_system.send(from_, to, message)

    def read(self, user):
        user.read()

    def read_all(self):
        for i in self.server.users:
            print(i.name)
            i.read()

    def get_server(self, name):
        for i in self.mail_system.servers:
            if i.name == name:
                return i


class ClientController(Controller):
    def __init__(self, mail_system):
        super().__init__(mail_system)
        self.client = None
        self.user = None

    def add_user(self, user):
        self.user = user
        self.mail_system.add_user(user)

    def add_client(self, client):
        self.client = client
        self.client.user = self.user

    def send(self, to, message):
        self.client.send(to, message)

    def receive(self, message):
        self.client.receive(message)

    def get_user(self):
        return self.user

    def read(self):
        self.client.read()


class ServerController(Controller):
    def __init__(self, mail_system):
        super().__init__(mail_system)
        self.server = None

    def add_server(self, server):
        self.server = server
        self.mail_system.add_server(server)

    def send(self, from_, to, message):
        self.mail_system.send(from_, to, message)

    def read(self, user):
        user.read()

    def read_all(self):
        for i in self.server.users:
            print(i.name)
            i.read()


class MailSystemController(Controller):
    def __init__(self, mail_system):
        super().__init__(mail_system)

    def add_server(self, server):
        self.mail_system.add_server(server)

    def add_user(self, user):
        self.mail_system.add_user(user)

    def send(self, from_, to, message):
        self.mail_system.send(from_, to, message)

    def read(self, user):
        user.read()

    def read_all(self):
        for i in self.server.users:
            print(i.name)
            i.read()


class Application:
    def __init__(self):
        self.mail_system = MailSystem()
        self.client_controller = ClientController(self.mail_system)
        self.server_controller = ServerController(self.mail_system)
        self.mail_system_controller = MailSystemController(self.mail_system)

    def get_client_controller(self):
        return self.client_controller

    def get_server_controller(self):
        return self.server_controller

    def get_mail_system_controller(self):
        return self.mail_system_controller


class ApplicationUI:
    def __init__(self, application):
        self.application = application
        self.client_controller = self.application.get_client_controller()
        self.server_controller = self.application.get_server_controller()
        self.mail_system_controller = self.application.get_mail_system_controller()

    def start(self):
        while True:
            print("1. Добавить пользователя")
            print("2. Добавить сервер")
            print("3. Отправить сообщение")
            print("4. Прочитать сообщения")
            print("5. Прочитать все сообщения")
            print("6. Выход")
            choice = int(input("Введите номер действия: "))
            if choice == 1:
                name = input("Введите имя пользователя: ")
                server_name = input("Введите имя сервера: ")
                server = self.mail_system_controller.get_server(server_name)
                user = User(name, server)
                self.client_controller.add_user(user)
                client = Client(user)
                self.client_controller.add_client(client)
            elif choice == 2:
                server = Server(input("Введите имя сервера: "))
                self.server_controller.add_server(server)
            elif choice == 3:
                to = User(input("Введите имя получателя: "))
                message = input("Введите сообщение: ")
                self.client_controller.send(to, message)
            elif choice == 4:
                self.client_controller.read()
            elif choice == 5:
                self.client_controller.read_all()
            elif choice == 6:
                break


def inject():
    app = Application()
    ui = ApplicationUI(app)
    return ui


if __name__ == "__main__":
    ui = inject()
    ui.start()
