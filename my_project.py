import json

# создаём функцию для загрузки тестов из файла
def load_tests(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# создаём функцию для вывода вопросов в консоли
def display_question(test):
    print(f"Текст: {test['текст']}\n")
    print(f"Вопрос: {test['вопрос']}\n")
    for i, option in enumerate(test['варианты'], 1):
        print(f"{i}. {option}")

# создаём функцию для проверки ответов
def check_answers(user_answers, correct_answers):
    user_answers_set = set(map(int, user_answers.split(',')))
    correct_answers_set = set(correct_answers)
    return user_answers_set == correct_answers_set

# создаём основную функцию
def main():
    # загружаем тесты из файла
    tests = load_tests('tests.json')

    right_answers = 0
    all_questions = 0

    for name, test in tests.items():
        print(f"\n{name}")
        display_question(test)
        user_answers = input("\nВведите номера верных ответов через запятую: ")
        if check_answers(user_answers, test['правильные_ответы']):
            print("Верно!")
            right_answers += 1
        else:
            print("Неверно!")
        all_questions += 1

    print(f'Вы ответили правильно на {right_answers} вопросов из {all_questions}.'
          f'\nХотите попробовать ещё раз? (Да/Нет)')

    # ждём, что ответит пользователь
    one_more_test = input('')
    # запускаем тест повторно, если пользователь отвечает 'Да'
    if one_more_test.lower() == 'да':
        main()

# запускаем основную функцию
if __name__ == "__main__":
    main()