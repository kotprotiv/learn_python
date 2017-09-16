with open('referat.txt', 'r', encoding='utf-8') as f:
    string = f.read()
    string = string.replace('\n', ' ')
    mass = string.split(' ')
    print(mass)
    print(len(mass))