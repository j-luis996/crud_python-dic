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
            print("this function updates an element")
        elif command == 'D':
            print("this function updates an element")
        else:
            if command != 'E':
                print('command invalid')
        if command != 'E':
            input('press any key for continue')


if __name__ == "__main__":
    main()