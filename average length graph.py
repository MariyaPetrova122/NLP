import urllib.request
import json
import re
import matplotlib.pyplot as plt


all_texts = []
tell_me_length = {}
public_list = [-57571503,-139105204,-102037283]
list_to_words = {'-57571503':'Прокаженный','-139105204':'хайер скул оф мемс','-102037283':'ЛАБОРАТОРИЯ КАРЬЕРЫ'}

for i in public_list:
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id='+str(i)+'&count=20&v=5.73&access_token=a668f74fa668f74fa668f74ff8a609a902aa668a668f74ffce5bd30c5037f0703eaf946')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    vk_result = json.loads(result)
    sum_length = 0
    for r in range(0,20):
        text = vk_result['response']['items'][r]['text']
        length = len(text.split(' '))
        sum_length+=length
        all_texts.append(text)
    av_length = sum_length//20
    print(av_length)
    tell_me_length[i] = av_length

print(tell_me_length)
average_length=[]
publos = []
names = []
for element in tell_me_length.keys():
    publos.append(element)

for thing in publos:
    average_length.append(tell_me_length[thing])

for thing in list_to_words:
    names.append(list_to_words[thing])

for i in range(len(publos)):
    publos[i]=publos[i]//10**6

plt.bar(publos, average_length,color='green')
plt.xticks(publos,names)
plt.show()

#f = open('texts.json','w', encoding='utf-8')
#json.dump(vk_result,f,indent=2,ensure_ascii=False)
#f.close()
'''
clean_text = []
for k in all_texts:
    reg = re.compile('[a-яА-Я]+')
    clean = reg.findall(k.lower())
    clean_text+=clean
'''
#print(clean_text,'\n',len(clean_text))
