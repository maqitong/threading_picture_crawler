import requests

"""
一、数据来源分析
    1、需求分析
        英雄名字——>对应图片
    2、接口分析
        第一层URL
        "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2816006"
        第二层
        "https://101.qq.com/#/hero-detail?heroid={从第一层获得}&datatype=5v5&tab=skin"
          协议protocol     ip:端口号     path路径        查询参数
        第三层
        id 构造出 图片的url
        "https://game.gtimg.cn/images/lol/act/img/js/hero/1.js?ts=2816008"

二、爬虫代码实现
    1、发送请求
    2、获取请求
    3、解析请求
    4、保存请求

"""


def find_json(url, headers):
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    return resp.json()


def parse_json(json_dic):
    result_list = []
    for item in json_dic['hero']:
        hero_name = item['name']
        hero_id = item['heroId']
        resp_dic = {
            "hero_name": hero_name,
            "hero_id": hero_id
        }

        result_list.append(resp_dic)

    return result_list


def save_json(hero_id):
    lst = []
    for item in hero_id:
        url_num = item['hero_id']
        url2 = f"https://game.gtimg.cn/images/lol/act/img/js/hero/{url_num}.js?ts=2816008"
        lst.append(url2)
    return lst


def main():
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2816006"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
    }
    json_dic = find_json(url, headers)
    hero_id = parse_json(json_dic)
    save_json(hero_id)


def run(url, headers):
    json_dic = find_json(url, headers)
    hero_id = parse_json(json_dic)
    url_list = save_json(hero_id)

    return url_list


if __name__ == '__main__':
    main()
