import requests
import picture_crawler as pc

def get_request_list(headers):
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2816006"

    detail_list = pc.run(url, headers)
    return detail_list


def parse_detail(detail_list, headers):
    pic_url_list = []

    try:
        for detail_url in detail_list[:10]:
            resp = requests.get(url=detail_url, headers=headers)
            for skin in resp.json()['skins']:
                dic = {}
                main_img = skin['mainImg']
                if main_img:
                    skin_name = skin['name']
                    dic['skin_name'] = skin_name
                    dic['main_img'] = main_img
                if dic:
                    pic_url_list.append(dic)

        return pic_url_list
    except:
        pass


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
    }
    detail_list = get_request_list(headers)
    pic_url_list = parse_detail(detail_list, headers)


def run():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
    }
    detail_list = get_request_list(headers)
    pic_url_list = parse_detail(detail_list, headers)
    return pic_url_list

if __name__ == '__main__':
    main()
