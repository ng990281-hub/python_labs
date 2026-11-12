import os
import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

OUT_PATH = "data/lab07/bench.csv"


def make_numbers(n):
    """Создаёт список из n случайных чисел."""
    return [random.randint(-1_000_000, 1_000_000) for _ in range(n)]


def measure(fn, number=1):
    """Измеряет среднее время выполнения функции."""
    return timeit.timeit(fn, number=number) / number


def bench_sorts():
    """Сравнивает три сортировки со sorted."""
    rows = []

    algorithms = [
        ("sorted", sorted),
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ]

    for n in (1_000, 10_000, 100_000):
        data = make_numbers(n)

        for name, fn in algorithms:
            if n > 10_000 and name != "sorted":
                seconds = "> 60 с (не запускалось)"
            else:
                seconds = f"{measure(lambda: fn(data)):.6f}"

            rows.append(("sort", n, name, seconds))

    return rows


def bench_search():
    """Сравнивает линейный и бинарный поиск."""
    data = make_numbers(100_000)
    queries = [random.choice(data) for _ in range(10_000)]

    rows = []

    # Линейный поиск
    def run_linear():
        for x in queries:
            linear_search(data, x)

    linear_time = measure(run_linear)
    rows.append(("search", 100_000, "linear_search", f"{linear_time:.6f}"))

    # Предварительная сортировка (нужна бинарному поиску)
    sort_time = measure(lambda: sorted(data), 10)
    sorted_data = sorted(data)
    rows.append(("search", 100_000, "sort_before_binary", f"{sort_time:.6f}"))

    # Бинарный поиск
    def run_binary():
        for x in queries:
            binary_search(sorted_data, x)

    binary_time = measure(run_binary)
    rows.append(("search", 100_000, "binary_search", f"{binary_time:.6f}"))

    # Сортировка плюс бинарный поиск
    rows.append(("search", 100_000, "binary+sort", f"{sort_time + binary_time:.6f}"))

    return rows


def bench_two_sum():
    """Сравнивает два решения задачи Two Sum."""
    rows = []

    for n in (1_000, 10_000):
        # Большой разброс значений: суммы почти не повторяются, поэтому
        # нужная пара единственная и стоит в конце списка (худший случай перебора).
        nums = [random.randint(0, 10**12) for _ in range(n)]
        target = nums[-2] + nums[-1]

        # Перебор пар
        brute_time = measure(lambda: two_sum_brute(nums, target))
        rows.append(("two_sum", n, "two_sum_brute", f"{brute_time:.6f}"))

        # Решение через словарь (быстрое: запускаем 100 раз и усредняем)
        fast_time = measure(lambda: two_sum_fast(nums, target), 100)
        rows.append(("two_sum", n, "two_sum_fast", f"{fast_time:.6f}"))

    return rows


def print_table(rows):
    """Выводит результаты в виде таблицы."""
    print(f"{'task':<10} | {'n':>8} | {'impl':<22} | {'seconds':>25}")
    print("-" * 75)

    last = None

    for task, n, impl, seconds in rows:
        if last is not None and (task, n) != last:
            print()

        print(f"{task:<10} | {n:>8} | {impl:<22} | {seconds:>25}")
        last = (task, n)


def main():
    random.seed(42)

    rows = []
    rows += bench_sorts()
    rows += bench_search()
    rows += bench_two_sum()

    print("\nРЕЗУЛЬТАТЫ БЕНЧМАРКА")
    print_table(rows)

    # Создаём папку, если её нет, и сохраняем результаты в CSV
    os.makedirs("data/lab07", exist_ok=True)
    write_csv(rows, OUT_PATH, header=("task", "n", "impl", "seconds"))

    print(f"\nРезультаты сохранены в {OUT_PATH}")


if __name__ == "__main__":
    main()
