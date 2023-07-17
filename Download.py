import requests
import picture2_crawler as pdp
import threading

pic_url_list = []


class DownloadPic(threading.Thread):

    def run(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
        }
        while pic_url_list:
            skin = pic_url_list.pop()
            # try:
            resp = requests.get(url=skin['main_img'], headers=headers)
            print(skin["skin_name"])
            with open(f'picture/{skin["skin_name"]}.jpg', 'wb') as f:
                f.write(resp.content)
            # except:
            #     pass


def main():
    global pic_url_list
    pic_url_list = pdp.run()

    for _ in range(2):
        thread = DownloadPic()
        thread.start()


if __name__ == '__main__':
    main()
