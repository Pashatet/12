import sys
inputfile = 'tests/rockyou.txt'

while True:
    try:
        print('Inside TRY')
        filename = open(inputfile, mode='r', encoding="latin-1") # какая-то поеботина с кодировкой
    except Exception: # проверка на все возможные ошбки
        print('Inside except')
        print('file not found')
        print(sys.exc_info())
        filename = input('enter correct file name:')
    else:
        print('Inside else')
        print(filename)
        sys.exit() # программа закрывается не обрабатываясь до конца 
    finally:
        print('Inside finaly')
print('YEP') 