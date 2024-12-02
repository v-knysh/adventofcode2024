import requests


def fetch_input(day):
    with open('cookie.txt') as f:
        cookie = f.read()
    input = requests.get(f'https://adventofcode.com/2024/day/{day}/input', headers={
        "Host": "adventofcode.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://adventofcode.com/2024/day/{day}",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    })
    data = input.content.decode('utf-8').split('\n')
    return data