def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data

  
def printinfo(data):
    for i in data:
        print(i)
        

def export(data):
    name = str(input('Введите имя и фамилию нового контакта (через пробел): '))
    with open('tel.txt', 'a', encoding='utf-8') as file:
        file.writelines(name)

def delete (data):
    name = input('Введите строку для удаления: ')
    with open('tel.txt', 'r', encoding='utf-8') as file:
        file.replace(name, '')
               
def main ():
    my_choice = -1
    data = readfile('tel.txt')
    while my_choice !=0:
        print('Выберете одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - произвести экспорт данных')
        print('3 - удаление пользователя')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {1: printinfo, 2: export, 3: delete}
        operations[my_choice](data)
        
    print ('До свидания')
    
if __name__ == '__main__':
    main()