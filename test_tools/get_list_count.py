import time
import requests


def get_current_time():
    return int(time.time())


def get_items_count():
    params = {'uid': 'fanq25bef785c9f113eb0b5d50138c87d3c7',
              'uid2': 'fanq25bef785c9f113eb0b5d50138c87d3c7',
              'eid': 'fanq25bef785c9f113eb0b5d50138c87d3c7',
              'sign': 'llq',
              'version': '8.2.0.116',
              'market': 'nh0001',
              'news_sdk_version': '2.0.12',
              'stype': 'portal',
              'net': '4',
              'sdkv': '3',
              'device': '3',
              'v': '1',
              'sv': '12',
              'n': '20',
              'newest_showtime': get_current_time() - 2,
              'oldest_showtime': get_current_time() - 1,
              'c': 'youlike',
              'scene': '9001',
              'sub_scene': '1',
              'refer_scene': '0',
              'refer_subscene': '14',
              'action': '0',
              'user_mode': '1',
              's_enid': '',
              's_dn': 'TUkgTUFY',
              's_av': '7.0',
              'performance': '',
              'brand': 'WGlhb21p',
              'uform': '1',
              'tj_deeplink': '1',
              'imgtype': '1',
              }
    base_url = 'http://sdk.look.360.cn/sdkv2/list'
    resp = requests.get(base_url, params=params)
    print(resp.json()['data']['res'])
    return resp.json()['data']['res'].__len__()


def run():
    for i in range(0, 100):
        c = get_items_count()
        print(c)


run()
