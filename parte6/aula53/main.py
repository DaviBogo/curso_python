
with open('abc.txt', 'w+') as file:
    file = open('abc.txt', 'w+')
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read(), end='')

    print('#########')

    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')

print('#########')

with open('abc.txt', 'r') as file:
    print(file.read())
