n=int(input("N: "))
t,f=0,0
for i in range(n):
    a=input(f'in_{i+1}: ')
    a=a.split()
    if len(a)!=4:
        continue
    else:
        if a[-1]=='True':
            t+=1
        else:
            f+=1

print(f'out: {t} {f}')          
    
