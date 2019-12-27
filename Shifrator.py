# -*- coding: utf-8 -*-
def coding (st, key): #кодирование Цезарь
    s = list(st)
    for i in range(len(s)):
        j = ord(s[i])
        j += key
        j = chr(j)
        s[i] = j

    return(''.join(s))
    
def decoding (st, key): #декодирование Цезарь
    s = list(st)
    for i in range(len(s)):
        j = ord(s[i])
        j -= key
        j = chr(j)
        s[i] = j
    return(''.join(s))
    
def find_key (st): #поиск клюса Цезарь
    s = list(st)
    d = {}
    for i in range(len(s)):
        try:
            d[s[i]] += 1
        except:
            d[s[i]] = 1
    print (d)
    mx = 0
    for k in d.keys():
        if d[k] > mx:
            mx = d[k]
            let = k
    print(mx)
    print(let)
    key = ord(let) - ord(" ")
    print(key)
    s = decoding(st, key)
    return s

def coding_v(st, key): #кодирование Виженером
    s = list(st)
    k = list(key)
    for i in range(len(k)):
        k[i] = ord(k[i])
    print(k)
    g = 0
    for i in range(len(s)):
        true_key = k[g % len(k)]
        j = ord(s[i]) 
        j += true_key
        j = chr(j % 255)
        s[i] = j
        g += 1
    st = ''
    for i in s:
        st += i
    return st
    
def decoding_v(st, key): #декодирование Виженер
    s = list(st)
    k = list(key)
    for i in range(len(k)):
        k[i] = ord(k[i])
    print(k)
    g = 0
    for i in range(len(s)):
        true_key = k[g % len(k)]
        j = ord(s[i]) 
        j -= true_key
        j = chr(j % 255)
        s[i] = j
        g += 1
    st = ''
    for i in s:
        st += i
    return st

msg = "Other collaborative online encyclopedias were attempted before Wikipedia, but none were as successful.[29] Wikipedia began as a complementary project for Nupedia, a free online English-language encyclopedia project whose articles were written by experts and reviewed under a formal process.[30] It was founded on March 9, 2000, under the ownership of Bomis, a web portal company. Its main figures were Bomis CEO Jimmy Wales and Larry Sanger, editor-in-chief for Nupedia and later Wikipedia.[31][32] Nupedia was initially licensed under its own Nupedia Open Content License, but even before Wikipedia was founded, Nupedia switched to the GNU Free Documentation License at the urging of Richard Stallman.[33] Wales is credited with defining the goal of making a publicly editable encyclopedia,[34][35] while Sanger is credited with the strategy of using a wiki to reach that goal.[36] On January 10, 2001, Sanger proposed on the Nupedia mailing list to create a wiki as a 'feeder' project for Nupedia."
new = coding(msg,3)
print(find_key(new))
msg = "Other collaborative online encyclopedias were attempted before Wikipedia, but none were as successful.[29] Wikipedia began as a complementary project for Nupedia, a free online English-language encyclopedia project whose articles were written by experts and reviewed under a formal process.[30] It was founded on March 9, 2000, under the ownership of Bomis, a web portal company. Its main figures were Bomis CEO Jimmy Wales and Larry Sanger, editor-in-chief for Nupedia and later Wikipedia.[31][32] Nupedia was initially licensed under its own Nupedia Open Content License, but even before Wikipedia was founded, Nupedia switched to the GNU Free Documentation License at the urging of Richard Stallman.[33] Wales is credited with defining the goal of making a publicly editable encyclopedia,[34][35] while Sanger is credited with the strategy of using a wiki to reach that goal.[36] On January 10, 2001, Sanger proposed on the Nupedia mailing list to create a wiki as a 'feeder' project for Nupedia."
key = "key"
print(msg)
new = coding_v(msg, key)
print(new)
print(decoding_v(new,key))
