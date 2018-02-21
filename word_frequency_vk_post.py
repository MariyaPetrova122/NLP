import urllib.request
import json
import re
all_texts = []

users_list = [37135110,33815655]
for i in users_list:
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id='+str(i)+'&count=5&v=5.73&access_token=a668f74fa668f74fa668f74ff8a609a902aa668a668f74ffce5bd30c5037f0703eaf946')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    vk_result = json.loads(result)
    for i in range(0,5):
        text = vk_result['response']['items'][i]['text']
        all_texts.append(text)

#f = open('texts.json','w', encoding='utf-8')
#json.dump(vk_result,f,indent=2,ensure_ascii=False)
#f.close()

clean_text = []
for k in all_texts:
    reg = re.compile('[a-яА-Я]+')
    clean = reg.findall(k.lower())
    clean_text+=clean

print(clean_text,'\n',len(clean_text))

from collections import Counter
d = Counter(clean_text)

print(d)


