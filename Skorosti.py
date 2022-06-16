import multiprocessing


def get_value():
    name = multiprocessing.current_process().name
    print(f"[{name}] numele")

if __name__ == '__main__':
    while 1:
        with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
            get_value()


