acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition of this acronym?\n')
with open('acronyms.txt', 'a') as file:
    file.write(f'{acronym}: {definition}\n')

look_up = input('What acronym do you want to look up?\n')
with open('acronyms.txt') as file:
    found = False
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
    if not found:
        print('Not found')

def main():
    print('Welcome to the acronym lookup program!')
    while True:
        print('\nOptions:')
        print('1. Look up an acronym')
        print('2. Add a new acronym')
        print('3. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            look_up = input('What acronym do you want to look up?\n')
            with open('acronyms.txt') as file:
                found = False
                for line in file:
                    if look_up in line:
                        print(line)
                        found = True
                        break
                if not found:
                    print('Not found')
        elif choice == '2':
            acronym = input('What acronym do you want to add?\n')
            definition = input('What is the definition of this acronym?\n')
            with open('acronyms.txt', 'a') as file:
                file.write(f'{acronym}: {definition}\n')
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()