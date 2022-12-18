def main():
    stop = ('.', 'good bye', 'close', 'exit', 'break')

    work = ('hello', 'add', 'change', 'phone', 'show all')

    while True:
        string = input().lower()
        print(string)
        answer = None
        if string.startswith(stop):
            print('Good bye!')
            break
        elif string.startswith(work):
            print(f'working: {string}')
            answer = handler(string)
            print(answer)
        else:
            print('Wrong input. Try agane.')


contacts = {'Oleg': ['380674020405',],
            'Olena': ['+380675096294',],
            'Oleksij': ['063-455-62-72',]
            }
            
def handler(string):
    work_list = string.split()
    print(work_list)
#    contacts = dict()
    if string.startswith('hello'):
        return 'How can I help you?'

    elif string.startswith('add'):
        return handler_add(string)
        

    elif string.startswith('change'):
        return handler_change(string)
        
    elif string.startswith('phone'):
        return handler_phone(string)
        

    else:
        return handler_show_all(string)

        

def handler_add(string):
    work_list = string.split()
    try:
        name = work_list[1]
        number_phone = work_list[2]
    except:
        print('add')
    
    else:
        if name.capitalize() in contacts:
                contacts[name.capitalize()].append(number_phone)
                return 'This name already exists! Number successfully added.'
        else:
            contacts[name.capitalize()] = []
            contacts[name.capitalize()].append(number_phone)
            return 'Contact successfully added.'

def handler_change(string):
    work_list = string.split()
    try:
        name = work_list[1]
        number_phone_old = work_list[2]
        number_phone_new = work_list[3]

    except:
        print('change')

    else:
        if work_list[1].capitalize() in contacts:
            if work_list[2] in contacts[work_list[1].capitalize()]:
                contacts[name.capitalize()].remove(number_phone_old)
                contacts[name.capitalize()].append(number_phone_new)
        return 'Contact successfully changed.'


def handler_phone(string):
    work_list = string.split()
    try:
        name = work_list[1]

    except:
        print('phone')

    else:
        return name.capitalize() + ' ' + f'{contacts[name.capitalize()]}'

def handler_show_all(string):
    return contacts


main()