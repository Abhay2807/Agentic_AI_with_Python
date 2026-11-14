# Threading example of making web requests

import threading
import requests
import time

def download_images(url):
    print(f"Starting image download from {url} ")
    response = requests.get(url)
    print(f"Image downloaded from {url}, file size : {len(response.content)} bytes")

image_urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start_time = time.time()
threads = []

for url in image_urls:
    t= threading.Thread(target=download_images, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end_time = time.time()
print(f"Total process took {end_time-start_time} seconds")



 
