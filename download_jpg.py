import urllib.request
import threading
import os


def download_book(_secret_key, _max_page_num, _level, _subject):
    p_dir = f'./{_subject}'
    c_dir = f'{p_dir}/{_level}'
    if not os.path.exists(p_dir):
        os.mkdir(p_dir)
    if not os.path.exists(c_dir):
        os.mkdir(c_dir)

    _max_page_num = int(_max_page_num)

    x = 1
    lock = threading.Lock()
    threads = []
    while True:
        with lock:
            for i in range(8):
                if x > _max_page_num:
                    break
                t = threading.Thread(target=download_image, args=(c_dir, _secret_key, x,))
                t.start()
                threads.append(t)
                x += 1

        for t in threads:
            t.join()
        threads = []

        if x > _max_page_num:
            break


def download_image(img_dir, _secret_key, index):
    img_url = f"https://book.pep.com.cn/{_secret_key}/files/mobile/" + str(index) + ".jpg?230907161620"
    urllib.request.urlretrieve(img_url, f'{img_dir}/%s.jpg' % index)
    print("download " + str(index) + " finished.")


class Book:
    subject = "政治"
    level = "九下"
    max_page_num = 100
    secret_key = "1384001302181"

    def __init__(self, subject, level, max_page_num, secret_key):
        self.subject = subject
        self.level = level
        self.max_page_num = max_page_num
        self.secret_key = secret_key

    def download_to_pc(self):
        download_book(self.secret_key, self.max_page_num, self.level, self.subject)


if __name__ == '__main__':
    books = [
        Book("地理", "七上", "114", "1338001101121"),
        Book("地理", "七下", "112", "1338001102121"),
        Book("地理", "八上", "122", "1338001201131"),
        Book("地理", "八下", "116", "1338001202131"),

        Book("地理", "必1", "134", "1438001121191"),
        Book("地理", "必2", "134", "1438001122191"),
        Book("地理", "选1", "106", "1438001131201"),
        Book("地理", "选2", "102", "1438001132201"),
        Book("地理", "选3", "128", "1438001133201"),
    ]
    for book in books:
        book.download_to_pc()
