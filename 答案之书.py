import requests
from bs4 import BeautifulSoup
import re
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'cookie': 'Hm_lvt_8489c97632ae8fa5be637f8d7d7f8a70=1742134657; Hm_lpvt_8489c97632ae8fa5be637f8d7d7f8a70=1742134657; HMACCOUNT=D7C30A14AC3C025E; Hm_lvt_5f28dcc076e02b498e45532b13cd6c13=1742134657; Hm_lpvt_5f28dcc076e02b498e45532b13cd6c13=1742134657',
}
url = 'http://www.lizhi135.com/articles/lizhi-258358.html'
response = requests.get(url=url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
sentences = []
declaration = '声明 :本网站尊重并保护知识产权，根据《信息网络传播权保护条例》，如果我们转载的作品侵犯了您的权利,请在一个月内通知我们，我们会及时删除。'

for p in soup.find_all('p'):
    sentence = p.get_text().strip()
    if sentence:
        sentence = re.sub(r'^\d+[.、]', '', sentence).strip()
        sentence = sentence.replace(declaration, '').strip()
        if sentence:
            sentences.append(sentence)
if sentences:
    sentences.pop()
try:
    user_input = int(input("请输入一个数字："))
    if sentences:
        random_sentence = random.choice(sentences)
        print(f"{random_sentence}")
    else:
        print("提取的句子列表为空，无法弹出句子。")
except ValueError:
    print("输入无效，请输入一个有效的整数。")