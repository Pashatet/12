inputfile = 'tests/rockyou.txt'
outputfile = 'tests/mypasswords.txt'

filename = open(inputfile, mode='r', encoding='latin_1')
filename2 = open(outputfile, mode='w', encoding='latin_1')

vasya='pasha'

for num, line in enumerate(filename, 1):
    if vasya in line:
        print('line № ', str(num),' Hello ', line.strip())
        filename2.write('found password: ' + line)

filename.close()
filename2.close()