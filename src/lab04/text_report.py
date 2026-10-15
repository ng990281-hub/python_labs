import sys

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
input_text="data/lab04/input.txt"

def sorted_words(freq):
    return sorted(freq.items(),key=lambda x: (-x[1],x[0]))

def main():
    try:
        text = read_text(input_text, encoding="utf-8")
    except FileNotFoundError:
        print("файл не найден")
        sys.exit(1)
        
    normal=normalize(text)
    token=tokenize(normal)
    freq=count_freq(token)
    top=top_n(freq,5)
    write_csv(sorted_words(freq),"data/lab04/report.csv", header=("word", "count"))

    print(f'Всего слов: {len(token)}')
    print(f'Уникальных слов: {len(freq)}')
    print("Топ-5:")
    for w,c in top:
        print(f'{w}:{c}')
if __name__ == "__main__":
    main()
