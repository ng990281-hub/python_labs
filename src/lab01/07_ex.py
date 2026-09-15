s=input('in: ')
for i in range(len(s)):
    if s[i].isupper():
        break
    
for j in range(i,len(s)):
    if s[j] in '0123456789':
        k=j+1-i
        break
t=s[j:].find('.')+len(s[:j])
ans=s[i]
for c in range(j+1,t,k):
    ans+=s[c]
print(f'out: {ans}.')
    
