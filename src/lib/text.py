import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text=text.casefold()
    if casefold==False:
        text=text.lower()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    text=text.replace('\t',' ').replace('\r',' ')
    text=text.strip()
    text=' '.join(text.split())
    return text
def tokenize(text: str) -> list[str]:
    pattern=r"\w+(?:-\w+)*"
    return re.findall(pattern,text)
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for w in tokens:
        freq[w]=freq.get(w,0)+1
    return freq
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
      return sorted(freq.items(),key=lambda x: (-x[1],x[0]))[:n]

if __name__=='__main__':
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    print('Normalize tests:OK')
    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    print('Tokenize tests:OK')

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]
    

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print("Count_freq and top_n tests:OK")
    print('Успешно')
'''print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
print(count_freq(["a","b","a","c","b","a"]))
print(top_n(count_freq(["a","b","a","c","b","a"]), n=2))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2))'''















