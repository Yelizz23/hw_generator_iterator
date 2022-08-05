from iterator import MyIterList
from generator import flat_generator
from generator import any_nesting_level

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    any_nested_list = [
        ['a', 'b', 'c'],
        ['d', ['x', 'y', 'z'], 'e', 'f'],
        [10, 100, [False, None], [True]]
    ]

    print('Итератор, который принимает список списков, и возвращает их плоское представление:')
    for item in MyIterList(nested_list):
        print(item)
    print()
    flat_list = [item for item in MyIterList(nested_list)]  # Компрехеншн, который возвращает плоский список
    print(flat_list)
    print()
    print('Итератор, который принимает список списков (любой уровень вложенности):')
    for item in MyIterList(any_nested_list):
        print(item)
    print()

    print('Генератор, который принимает список списков, и возвращает их плоское представление:')

    for item in flat_generator(nested_list):
        print(item)
    print()
    print('Генератор обрабатывающий списки с любым уровнем вложенности:')

    for item in any_nesting_level(any_nested_list):
        print(item)
