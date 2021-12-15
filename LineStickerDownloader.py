import os

import requests, re

counter = 0
def get_stickers_list(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    req = requests.get(url=url, headers=headers).content.decode('utf-8')
    items = re.findall(r'data-preview=.*?(https.*?\.png)', req)

    return items

def download(list):
    global counter
    path = os.getcwd() + '\\LineStickers'
    if not os.path.exists(path):
        os.makedirs(path)
    for eachURL in list:
        img = requests.get(eachURL).content
        name = path + '\\' + str(counter) + '.png'
        counter += 1
        with open(name, 'wb') as h:
            h.write(img)



if __name__ == '__main__':
    url = ''
    while 1 :
        url = input("Enter the lineshop url: (enter 'exit' to exit')\n")
        if url == 'exit': exit(0)
        items = get_stickers_list(url=url)
        download(items)
        print('Download complete! Current file name counter: ' + str(counter))


