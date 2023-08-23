

import requests
from collections import Counter


if __name__ == '__main__':

    resp = requests.get("http://www.boredapi.com/api/activity/")
    # print(list(resp.json().keys()))
    print(Counter(list(resp.json().keys())) == Counter(['activity', 'accessibility', 'type', 'participants', 'price', 'link', 'key']))

