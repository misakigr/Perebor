from BazaBD import dbaza

mas = ('pubaddr1',
       'pubaddr1c',
       'pubaddr3',
       'pubaddrbc1_P2WPKH',
       'pubaddrbc1_P2WSH'
       )


def sel(wallet):
    wall = wallet.address.__dict__['mainnet'].__dict__
    for i in range(5):
        name = wall[mas[i]]
        #print(wall[mas[i]])
        dbaza(name, wallet)


# c = '1Misac'
# i = 4
# def sel(wallet):
#     wall = wallet.address.__dict__['mainnet'].__dict__
#
#     name = wall[mas[1]]
#     #print(c[:(i+1)])
#     # if c[:3] == name[:3]:
#     #     print('Исходниый текст: ', c[:3], 'сгенерированно: ', name[:3], 'Совпадение: 75%')
#     if c[:i] == name[:i]:
#         print('Исходниый текст: ', '--', c[:i], '--', 'Совпадение: 1%')
#     if c[:(i+1)] == name[:(i+1)]:
#         print('Исходниый текст: ', '--', c[:(i+1)], '--', 'Совпадение: 1.5%', name)