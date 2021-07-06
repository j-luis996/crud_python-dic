from ej import search_client
import const

class crud:
    def __get_client_field(self, field_name, message = "What's the client {}? "):
        field = None

        while not field:
            field = input(message.format(field_name))
        return field


    def __get_client_from_user(self):
        client = {
            'name': self.__get_client_field(field_name = 'name'),
            'company': self.__get_client_field(field_name = 'company'),
            'email': self.__get_client_field(field_name = 'email'),
            'position': self.__get_client_field(field_name = 'position'),
        }

        return client


    def __add_client(self, client):
        if client in const.clients:
            print("Client alredy in client's list")
        else:
            const.clients.append(client)


    def create_client(self):
        client = self.__get_client_from_user()
        self.__add_client(client)
        print('Added client successful')


    def read_clients(self):
        print('uid | name   |   company |   email   | position')
        print('*' * 50)

        for idx, client in enumerate(const.clients):
            print(f'{idx}  | {client["name"]}  | {client["company"]}  | {client["email"]}  | {client["position"]}')


    def update_client(self):
        id_client = int(self.__get_client_field(field_name="id"))
        if id_client < len(const.clients):
            client_update = self.__get_client_from_user()
            const.clients[id_client] = client_update
            print("Client updated in client's list")
        else:
            print('id invalid')


    def delete_client(self):
        id_client = int(self.__get_client_field(field_name="id"))
        if id_client < len(const.clients):
            for idx, client in enumerate(const.clients):
                if idx == id_client:
                    del const.clients[idx] 
                    break
            print("Client deleted in client's list")
        else:
            print('id invalid')


    def search_client(self, data, key = "name"):
        client_exist = False
        for client in const.clients:
            if client[key] ==data:
                client_exist = True
                break
            else:
                continue
        return client_exist