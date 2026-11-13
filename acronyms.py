with open('acronyms.txt') as file:
    found = False
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
    if not found:
        print('Not found')
