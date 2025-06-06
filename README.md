# Chyslivnyk - Бібліотека для українських числівників

`Chyslivnyk` - це Python-бібліотека, призначена для конвертації числових значень у їх текстові представлення українською мовою з урахуванням граматичних особливостей (відмінків, родів, чисел).

Ця бібліотека реалізована у вигляді класу `Chyslivnyk`, що дозволяє інкапсулювати логіку та дані, роблячи код більш структурованим.

**Важливо:** Ця бібліотека є базовою реалізацією. Відмінювання складних числівників в українській мові має багато нюансів, які можуть бути не повністю охоплені цією версією. Зокрема, повне відмінювання складених кількісних числівників (де всі компоненти змінюються) та складних порядкових числівників (де змінюється лише останній компонент) реалізовано спрощено або вимагає подальшого розширення словників та логіки.

## Установлення

```bash
pip install chyslivnyk
```

# Основне використання

Спочатку створіть екземпляр класу Chyslivnyk, а потім викликайте його методи. Імпортуйте необхідні константи (вони залишаються на рівні модуля для зручності):
```Python
from chyslivnyk import (
    Chyslivnyk, # Імпортуємо клас
    CASE_NOMINATIVE, CASE_GENITIVE, CASE_DATIVE, CASE_ACCUSATIVE, CASE_INSTRUMENTAL, CASE_LOCATIVE,
    GENDER_MASCULINE, GENDER_FEMININE, GENDER_NEUTER, NUMBER_PLURAL
)

# Створіть екземпляр класу
numerals_converter = Chyslivnyk()
```

# 1. Кількісні числівники (цілі)
Використовуйте метод Chyslivnyk.get_cardinal().

```Python
# Називний відмінок
print(numerals_converter.get_cardinal(1))                     # --> "один"
print(numerals_converter.get_cardinal(1, gender=GENDER_FEMININE)) # --> "одна"
print(numerals_converter.get_cardinal(5))                     # --> "п'ять"
print(numerals_converter.get_cardinal(25))                    # --> "двадцять п'ять"
print(numerals_converter.get_cardinal(101))                   # --> "сто один"
print(numerals_converter.get_cardinal(200))                   # --> "двісті"
print(numerals_converter.get_cardinal(1000))                  # --> "тисяча"
print(numerals_converter.get_cardinal(2000))                  # --> "дві тисячі"
print(numerals_converter.get_cardinal(12345678))              # --> "дванадцять мільйонів триста сорок п'ять тисяч шістсот сімдесят вісім"

# З родовим відмінком
print(numerals_converter.get_cardinal(25, case=CASE_GENITIVE)) # --> "двадцяти п'яти"
print(numerals_converter.get_cardinal(1, case=CASE_GENITIVE, gender=GENDER_FEMININE)) # --> "однієї"
print(numerals_converter.get_cardinal(40, case=CASE_INSTRUMENTAL)) # --> "сорока"
print(numerals_converter.get_cardinal(700, case=CASE_DATIVE)) # --> "семистам"
```

# 2. Збірні числівники
Використовуйте метод numerals_converter.get_collective(). Підтримує числа від 2 до 10.
```Python
print(numerals_converter.get_collective(2))                # --> "двоє"
print(numerals_converter.get_collective(5, case=CASE_GENITIVE)) # --> "п'ятьох"
print(numerals_converter.get_collective(7, case=CASE_INSTRUMENTAL)) # --> "сімома"
```

# 3. Дробові числівники
Використовуйте метод numerals_converter.get_fractional() для чисельника та знаменника, або numerals_converter.get_decimal_fractional() для десяткових дробів.
```Python
# З чисельником і знаменником
print(numerals_converter.get_fractional(1, 2))                     # --> "одна друга"
print(numerals_converter.get_fractional(3, 4, case=CASE_DATIVE))   # --> "трьом четвертим"
print(numerals_converter.get_fractional(2, 5, case=CASE_GENITIVE)) # --> "двох п'ятих"

# З десятковим дробом
print(numerals_converter.get_decimal_fractional(0.5))                 # --> "нуль цілих одна друга"
print(numerals_converter.get_decimal_fractional(3.14))                # --> "три цілих чотирнадцять сотих"
print(numerals_converter.get_decimal_fractional(1.25, case=CASE_INSTRUMENTAL)) # --> "однією цілою двадцятьма п'ятьма сотими"
```

# 4. Порядкові числівники
Використовуйте метод numerals_converter.get_ordinal().
```Python
print(numerals_converter.get_ordinal(1))                         # --> "перший"
print(numerals_converter.get_ordinal(1, gender=GENDER_FEMININE)) # --> "перша"
print(numerals_converter.get_ordinal(5, case=CASE_GENITIVE))     # --> "п'ятого"
print(numerals_converter.get_ordinal(7, gender=GENDER_NEUTER, case=CASE_INSTRUMENTAL)) # --> "сьомим"
print(numerals_converter.get_ordinal(21))                        # --> "двадцять перший"
print(numerals_converter.get_ordinal(21, gender=GENDER_FEMININE, case=CASE_DATIVE)) # --> "двадцять першій"
print(numerals_converter.get_ordinal(100))                       # --> "сотий"
print(numerals_converter.get_ordinal(101))                       # --> "сто перший"
print(numerals_converter.get_ordinal(121))                       # --> "сто двадцять перший"
print(numerals_converter.get_ordinal(1000, gender=GENDER_FEMININE)) # --> "тисячна"
print(numerals_converter.get_ordinal(1000, number_type=NUMBER_PLURAL)) # --> "тисячні"а"
```

## Особливості реалізації
* Клас Chyslivnyk: Вся логіка та дані інкапсульовані в одному класі.
* Обробка винятків: Методи викликають TypeError для некоректних типів вхідних даних та ValueError для недійсних граматичних параметрів або чисел поза підтримуваним діапазоном.
* Словники відмінювання: Використовуються внутрішні словники (тепер атрибути класу) для зберігання форм числівників у різних відмінках та родах. Це робить код більш читабельним та легким для розширення.
* Обмеження: Через складність української граматики, деякі аспекти (наприклад, повне відмінювання всіх складових частин дуже великих чисел або складених порядкових числівників типу "сто двадцять перший") реалізовано спрощено. Для повної академічної точності може знадобитися значне розширення словників та логіки.
* Мова: Весь код, коментарі та документація написані українською мовою.
