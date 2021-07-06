import os
import const

def main():
    command = None

    while command != 'E':
        os.system('clear')

        print(const.menu)

        command = input()
        command = command.upper()

        if command == 'C':
            print("this function will create a new element")
        elif command == 'R':
            print("this function will read the all list")
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