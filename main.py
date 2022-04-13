import requests
from threading import Thread, active_count
from random import randint, choice


def main(item_id):
    headers = {
        "content-type":
        "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent":
        "com.zhiliaoapp.musically.go/220400 (Linux; U; Android 10; en_US; SM-G9250; Build/MMB25K.G9250ZTU5DPC5; Cronet/TTNetVersion:5f9540e5 2021-05-20 QuicVersion:47555d5a 2020-10-15)"
    }
    url = f"https://{choice(ApiDomain)}/aweme/v1/aweme/stats/?channel=googleplay&device_type=SM-G9250&device_id{randint(1000000000000000000, 9999999999999999999)}&os_version=10&version_code=220400&app_name=musically_go&device_platform=android&aid=1988"
    Data = f"item_id={item_id}&share_delta=1"

    try:
        r.post(url, headers=headers, data=Data, stream=True)
    except:
        pass


if __name__ == "__main__":
    link_id = input('TikTok Link: ')
    ApiDomain = [
        "api19.tiktokv.com", "api.toutiao50.com", "api19.toutiao50.com",
        "api19-core-c-alisg.tiktokv.com"
    ]
    r = requests.Session()
    threads = 500
    print('Sending Shares to:', link_id)
    try:
        if "vm.tiktok.com" in link_id or "vt.tiktok.com" in link_id:
            link_id = r.head(link_id,
                             stream=True,
                             allow_redirects=True,
                             timeout=5).url.split("/")[5].split("?", 1)[0]
        else:
            link_id = link_id.split("/")[5].split("?", 1)[0]
    except:
        print('[*] Link not supported')
        quit()

    while True:
        if active_count() <= 5000:
            Thread(target=main, args=(link_id, )).start()
