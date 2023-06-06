import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()


# def do_sth():
#     print('sleeping 1 sec')
#     time.sleep(1)
#     print('done sleeping')

# Function with argument
def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'done sleeping {seconds}'

if __name__ == '__main__':
    # Oldway
    # p1 = multiprocessing.Process(target=do_sth)
    # p2 = multiprocessing.Process(target=do_sth)
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    # for many using loop
    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_sth)
    #     p.start()
    #     processes.append(p)
    #
    # for th in processes:
    #     th.join()

    # function with arguments

    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_sth, args=(1.5,))
    #     p.start()
    #     processes.append(p)
    #
    # for pr in processes:
    #     pr.join()

    # Faster way with concurrent
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_sth,1)
        # f2 = executor.submit(do_sth,1)
        # print(f1.result())
        # print(f2.result())
        secs = [5,4,3,2,1]
        # result = [executor.submit(do_sth,sec) for sec in secs]
        # for f in concurrent.futures.as_completed(result):
        #     print(f.result())

        result = executor.map(do_sth, secs)
        # for res in result:
        #     print(res)


    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)}')
