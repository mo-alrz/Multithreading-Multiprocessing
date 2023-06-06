import requests
import time
import threading
import concurrent.futures


imgurls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]


t1 = time.perf_counter()

def download(url):
    bytes = requests.get(url).content
    name = str(url.split('/')[3]) + '.jpg'
    with open(name, 'wb') as f:
        f.write(bytes)
        print(f'{name} was downloaded')


# with threading library
threads = []
for i in imgurls:
    t = threading.Thread(target=download, args=[i])
    t.start()
    threads.append(t)

for i in threads:
    i.join()

# with concurrent library
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download, imgurls)

t2 = time.perf_counter()
print(f'finished in {t2-t1} seconds')
