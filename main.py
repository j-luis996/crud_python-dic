import os
import const
import crud


crud = crud.crud()
def main():
    command = None

    while command != 'E':
        os.system('clear')

        print(const.menu)

        command = input()
        command = command.upper()

        if command == 'C':
            crud.create_client()
        elif command == 'R':
            crud.read_clients()
        elif command == 'U':
            crud.update_client()
        elif command == 'D':
            crud.delete_client()
        elif command == 'S':
            name = input('What is the client name? ')
            if crud.search_client(name):
                print("The client is in the client's list")
            else:
                print(f"The client: {name} is not in our client's list")
        else:
            if command != 'E':
                print('command invalid')
        if command != 'E':
            input('press any key for continue')


if __name__ == "__main__":
    main()