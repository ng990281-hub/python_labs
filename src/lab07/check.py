import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials

def check_search():
    """
    Проверяет функции linear_search и binary_search на случайных данных.
    Возвращает количество успешно пройденных испытаний.
    """
    trials = 100
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        x = random.randint(-60, 60)
        
        # Линейный поиск против list.index
        try:
            expected_lin = nums.index(x)
        except ValueError:
            expected_lin = -1
        actual_lin = linear_search(nums, x)
        assert actual_lin == expected_lin, f"linear_search ошиблась для поиска {x} в {nums}: получено {actual_lin}, ожидалось {expected_lin}"

        # Бинарный поиск
        sorted_nums = sorted(nums)
        try:
            expected_bin = sorted_nums.index(x)
        except ValueError:
            expected_bin = -1
        actual_bin = binary_search(sorted_nums, x)
        if expected_bin == -1:
            assert actual_bin == -1, f"binary_search не нашла элемент, которого нет: {x} в {sorted_nums}"
        else:
            assert actual_bin != -1 and sorted_nums[actual_bin] == x, f"binary_search вернула некорректный индекс {actual_bin} для {x} в {sorted_nums}"
    return trials


def check_two_sum(trials=100):
    """Оба two_sum дают пару с нужной суммой или оба None."""
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-30, 30) for _ in range(n)]
        target = random.randint(-60, 60)

        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)

        if a is None:
            assert b is None, f"Перебор не нашёл, словарь нашёл {b}"
            continue

        assert b is not None, f"Перебор нашёл {a}, словарь не нашёл"

        i, j = a
        assert nums[i] + nums[j] == target, f"brute вернул неверные индексы: {a}"
        i, j = b
        assert nums[i] + nums[j] == target, f"fast вернул неверные индексы: {b}"

    return trials

if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")





    
