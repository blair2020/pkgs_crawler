import time
import requests


t_start = time.time()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
url = 'http://archive.ubuntu.com/ubuntu/pool/main/t/tmux/tmux_3.0a-2_amd64.deb'
response = requests.get(url, headers=headers)
with open('tmux_3.0a-2_amd64.deb', 'wb') as f:
    f.write(response.content)
url2 = 'http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/libc6_2.31-0ubuntu9_amd64.deb'
response2 = requests.get(url2, headers=headers)
with open('libc6_2.31-0ubuntu9_amd64.deb', 'wb') as f:
    f.write(response2.content)
t_end = time.time()
print('耗时：', t_end - t_start)
