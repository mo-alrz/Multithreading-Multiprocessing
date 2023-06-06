import time
import threading
import concurrent.futures

start = time.perf_counter()


def do_sth():
    print('sleeping 1 second')
    time.sleep(1)
    print('done sleeping')


# old way :
t1 = threading.Thread(target=do_sth)
t2 = threading.Thread(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()

# for many using loop
threads = []
for _ in range(10):
    t = threading.Thread(target=do_sth)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


# function with arguments
def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('done sleeping')


threads = []
for _ in range(10):
    t = threading.Thread(target=do_sth, args=[1.5])
    t.start()
    threads.append(t)

for th in threads:
    th.join()


# Faster way
def do_sth(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'done sleeping {seconds}'


with concurrent.futures.ThreadPoolExecutor() as executer:
    f1 = executer.submit(do_sth,1)
    f2 = executer.submit(do_sth, 1)
    print(f1.result())
    print(f2.result())

    # many times with multiple args:
    secs = [5, 4, 3, 2, 1]
    result = [executer.submit(do_sth, sec) for sec in secs]
    for f in concurrent.futures.as_completed(result):
        print(f.result())

finish = time.perf_counter()
print(f'{round(finish - start, 2)}')
