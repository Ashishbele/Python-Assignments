'''try:
    file1 = open('sample.txt', 'r')

    for line in file1:
        print(line.strip())

    file1.close()
except FileNotFoundError:
    print('Error : The Sample.txt file was not found')'''

try:
    file1 = open('sample.txt', 'r')
    reading = file1.read()
    print(reading)
    file1.close()
except FileNotFoundError:
    print('Error : The Sample.txt file was not found')


