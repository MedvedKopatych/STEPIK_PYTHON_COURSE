import re
import requests


"""place = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
link = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'


def get_links(url):
    pattern = r'.a.*href="(.+)\".*a\>'
    res = requests.get(url)
    if res.status_code == 200:
        res_match = re.findall(pattern, res.text)
        return res_match
    else:
        return []


def steps():
    first_step = get_links(place)
    print(first_step, "first")
    for elem in first_step:
        print(elem)
        second_step = get_links(elem)
        print(second_step, "second")
        if link in second_step:
            return True
    return False


if steps():
    print('Yes')
else:
    print('No')
"""




import re
import urllib.request
from urllib.parse import urlparse

url = 'http://pastebin.com/raw/7543p0ns'


def get_links():
    try:
        res = requests.get(url)
        if res.status_code == 200:
            links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', res.text)
    except res.status_code != 200:
        return []
    else:
        return links


def parse_link(link):
    parsed_url = urlparse(link)
    adress = parsed_url.netloc
    try:
        return adress[:adress.index(':')]
    except:
        return adress
    else:
        return adress[:adress.index(':')]


links = get_links()

unsorted = list(map(parse_link, links))
print(unsorted)

for link in sorted(list(set(unsorted))):
    print(link)
