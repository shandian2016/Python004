# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

# from fake_useragent import UserAgent
# ua = UserAgent(verify_ssl=False)

#import re
header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36','Cookie':'__mta=20356615.1601101382923.1601130090143.1601130119086.9; uuid_n_v=v1; uuid=9F4340D0FFC011EA8D33277AD0CAC56A06EAAF53719E408FB9CAD53031F7FD1E; mojo-uuid=aec9a7a6861931b9a7c76ee77d2f70f2; _lxsdk_cuid=174c914448ec8-00dc31c1b97165-3a36570a-100200-174c914448f49; _lxsdk=9F4340D0FFC011EA8D33277AD0CAC56A06EAAF53719E408FB9CAD53031F7FD1E; _csrf=99942cb96af08a093adec9538c19ad649ca7dbafe908dccd82187dda856fdc5d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601553323,1601626114,1601695149,1601801645; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601801645; __mta=20356615.1601101382923.1601130119086.1601801644977.10; _lxsdk_s=174f2d16b37-d31-920-f7%7C%7C2'}
#header = {'user-agent':ua.random}
url = 'https://maoyan.com/films?showType=3'
response = requests.get(url,headers=header)
bs_info = bs(response.text, 'html.parser')
response.encoding = 'utf8'
#print(response.text)

lb = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'},limit=10):
    dymc = tags.find('span',attrs={'class':'name'}).text
    dylx = tags.find_all('div',attrs={'class':'movie-hover-title'})[1].contents[2].strip()
    #dylx = re.sub(r'类型:|\s','',dylx1)
    dysj = tags.find('div',attrs={'class':'movie-hover-title movie-hover-brief'}).contents[2].strip()
    #dysj = re.sub(r'上映时间:\s','',dysj1)
    lb_1 = [dymc,dylx,dysj]
    lb.append(lb_1)

import pandas as pd

zuoye1 = pd.DataFrame(data = lb)

zuoye1.to_csv('./zuoye1.csv', encoding='utf_8_sig', index=False, header=False)