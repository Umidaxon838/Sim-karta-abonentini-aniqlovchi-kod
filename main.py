num = input('Enter num: ')
code = num[4:6]
if num[1:].isnumeric() and len(num) == 13 and num[1:4] == '998':
    if code == '90' or code == '91':
        print('Sizning operatoriz Beline')
    elif code == '93' or code == '94' or code == '98':
        print('Sizning operatoriz Ucell')
    elif code == '88':
        print('Sizning operatoriz MobiUz')
    elif code == '33':
        print('Sizning operatoriz Humans')
    elif code == '66':
        print('Sizning operatoriz Uztelecom')
    elif code == '95' or code == '99':
        print('Sizning operatoriz Uzmobile')
    else:
        print('Ты крыса что ли')
elif num == '+12566938911':
    print('This is Максим Орлов')
else:
    print('Raqam xato kiritildi!')
