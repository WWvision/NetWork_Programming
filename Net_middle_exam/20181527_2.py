link = 'https://search.daum.net/search?w=tot&q=bigdata'
spl1 = link.split('?')
spl2 = spl1[1].split('&')
dict_val = {}
for i in spl2:
    spl3 = i.split('=')
    dict_val[spl3[0]] = spl3[1]
#첫번째출력
print(dict_val) 

#두번째출력
dict_val['q'] = 'iot'
print(dict_val)
    
    