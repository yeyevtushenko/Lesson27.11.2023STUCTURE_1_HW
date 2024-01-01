def main():
    numbers = []

    while True:
        print("\nМеню:")
        print("1. Додати нове число до списку")
        print("2. Видалити усі входження числа зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("0. Вийти з програми")

        choice = input("Виберіть опцію (0 вихід з програми): ")
        if choice == "1":
            add_number(numbers)
        elif choice == "2":
            remove_number(numbers)
        elif choice == "3":
            show_list(numbers)
        elif choice == "4":
            check_value(numbers)
        elif choice == "5":
            replace_value(numbers)
        elif choice == "6":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

def add_number(numbers):
    number = int(input("Введіть число для додавання: "))
    if number not in numbers:
        numbers.append(number)
        print(f"Число {number} додано до списку.")
    else:
        print(f"Число {number} вже існує у списку.")

def remove_number(numbers):
    number_to_remove = int(input("Введіть число для видалення: "))
    if number_to_remove in numbers:
        numbers = [x for x in numbers if x != number_to_remove]
        print(f"Усі входження числа {number_to_remove} видалено зі списку.")
    else:
        print(f"Число {number_to_remove} не знайдено у списку.")

def show_list(numbers):
    reverse_order = input("Вивести список у зворотньому порядку? (y/n): ")
    if reverse_order.lower() == 'y':
        numbers.reverse()
        print("Список чисел:", numbers)

def check_value(numbers):
    value_to_check = int(input("Введіть число для перевірки: "))
    if value_to_check in numbers:
        print(f"Число {value_to_check} знайдено у списку.")
    else:
        print(f"Число {value_to_check} не знайдено у списку.")

def replace_value(numbers):
    value_to_replace = int(input("Введіть число, яке потрібно замінити: "))
    new_value = int(input("Введіть нове число: "))
    replace_all = input("Замінити всі входження? (y/n): ")

    if replace_all.lower() == 'y':
        numbers = [new_value if x == value_to_replace else x for x in numbers]
        print(f"Всі входження числа {value_to_replace} замінено на {new_value}.")
    else:
        if value_to_replace in numbers:
            index = numbers.index(value_to_replace)
            numbers[index] = new_value
            print(f"Перше входження числа {value_to_replace} замінено на {new_value}.")
        else:
            print(f"Число {value_to_replace} не знайдено у списку.")
















