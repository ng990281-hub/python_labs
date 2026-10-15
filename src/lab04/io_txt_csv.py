import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл целиком и возвращает его содержимое одной строкой.

    По умолчанию используется кодировка UTF-8.
    Для другой кодировки можно передать её явно, например:
    encoding="cp1251".

    Если файл не существует, всплывает FileNotFoundError.
    Если кодировка не подходит, всплывает UnicodeDecodeError.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)
def ensure_parent_dir(path: str | Path):
    """
    Создаёт родительские директории для указанного пути,
    если они ещё не существуют.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if len(rows)>0:
        l1=len(rows[0])
        for row in rows:
            if len(row)!=l1:
                raise ValueError("Все строки должны иметь одинаковую длину")
        if header is not None and len(header)!=l1:
            raise ValueError("Длина заголовка должна совпадать с длиной строк")
    ensure_parent_dir(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    print(txt)
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")







            
