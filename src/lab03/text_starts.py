import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
flag=1
text=sys.stdin.read()
if text.strip()=='':
    raise ValueError("Пустой текст")
norm=normalize(text)
token=tokenize(norm)
cf=count_freq(token)
top=top_n(cf,n=5)
print('Всего слов:',len(token))
print('Уникальных слов:',len(set(token)))
print('Топ-5:')
if not flag:
    for t,c in top:
        print(f'{t}:{c}')
else:
    mx_sl=max(len(t) for t,c in top)
    mx=max(mx_sl,len('слово'))
    head=f'{"слово":<{mx}} | частота'
    print(head)
    print('-'*len(head))
    for t,c in top:
        print(f'{t:<{mx}} | {c}')

