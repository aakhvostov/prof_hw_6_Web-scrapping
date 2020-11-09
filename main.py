import requests
from bs4 import BeautifulSoup

response = requests.get('https://2ip.ru/')


ip_id = response.text.find('id="d_clip_button"')
ip_start_pos = response.text.find('<span>', ip_id) + 6
ip_stop_pos = response.text.find('</', ip_start_pos)

ip = response.text[ip_start_pos:ip_stop_pos]
print(ip)

ret = requests.get('https://2ip.ru/')


soup = BeautifulSoup(ret.text, 'html.parser')
el = soup.find(id="d_clip_button")

ip_b = el.text
print(ip_b)
