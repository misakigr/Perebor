# author: 'Misac'
# license: GPL3
"""This is the "example" module.
"""

import Wifgen
import SelectAdress
# import time
import multiprocessing


def main():
    try:
        wallet = Wifgen.wif()
        SelectAdress.sel(wallet)
    except:
        pass


if __name__ == '__main__':
    while 1:
        # start_time = time.time()
        with multiprocessing.Pool(multiprocessing.cpu_count()+2) as p:
            main()



        # print("--- %s seconds ---" % (time.time() - start_time))

