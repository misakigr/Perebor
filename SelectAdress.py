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