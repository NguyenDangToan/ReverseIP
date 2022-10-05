import sys
import requests
from bs4 import BeautifulSoup as bs
import urllib3
urllib3.disable_warnings()


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <ip>" %sys.argv[0])
        sys.exit()
    ip = sys.argv[1]

    #reverse_ip
    url = "https://dnslytics.com/reverse-ip"
    data = "reverseip=%s" %ip
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0','Content-Type': 'application/x-www-form-urlencoded'}
    proxies = {"http":"127.0.0.1:8080", "https":"127.0.0.1:8080"}
    res = requests.post(url, data, headers=headers, verify=False, proxies=proxies)

    #print(res.text)

    soup = bs(res.text, 'html.parser')
    myTable = soup.find('table',{'class':'table table-condensed table-hover'})
    for x in myTable.find_all('tr'):
        td_tags = x.find_all('td')
        td_val = [y.text for y in td_tags]
        if len(td_val) == 3:
            print(td_val)
            

if __name__ == '__main__':
    main()
