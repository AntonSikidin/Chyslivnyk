import unittest
from Chyslivnyk import (
    Chyslivnyk, # Імпортуємо клас
    CASE_NOMINATIVE, CASE_GENITIVE, CASE_DATIVE, CASE_ACCUSATIVE, CASE_INSTRUMENTAL, CASE_LOCATIVE,
    GENDER_MASCULINE, GENDER_FEMININE, GENDER_NEUTER, NUMBER_PLURAL
)

class TestNumeralsUA(unittest.TestCase):

    def setUp(self):
        """Ініціалізація екземпляра класу перед кожним тестом."""
        self.chyslivnyk = Chyslivnyk()

    # --- Тести для get_cardinal (цілі кількісні) ---
    def test_cardinal_basic(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(1), "один")
        self.assertEqual(self.chyslivnyk.get_cardinal(1, gender=GENDER_FEMININE), "одна")
        self.assertEqual(self.chyslivnyk.get_cardinal(1, gender=GENDER_NEUTER), "одне")
        self.assertEqual(self.chyslivnyk.get_cardinal(2, gender=GENDER_FEMININE), "дві")
        self.assertEqual(self.chyslivnyk.get_cardinal(2), "два") # Чоловічий/середній за замовчуванням
        self.assertEqual(self.chyslivnyk.get_cardinal(5), "п'ять")
        self.assertEqual(self.chyslivnyk.get_cardinal(0), "нуль")

    def test_cardinal_tens(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(10), "десять")
        self.assertEqual(self.chyslivnyk.get_cardinal(15), "п'ятнадцять")
        self.assertEqual(self.chyslivnyk.get_cardinal(20), "двадцять")
        self.assertEqual(self.chyslivnyk.get_cardinal(21), "двадцять один")
        self.assertEqual(self.chyslivnyk.get_cardinal(21, gender=GENDER_FEMININE), "двадцять одна")
        self.assertEqual(self.chyslivnyk.get_cardinal(40), "сорок")
        self.assertEqual(self.chyslivnyk.get_cardinal(99), "дев'яносто дев'ять")

    def test_cardinal_hundreds(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(100), "сто")
        self.assertEqual(self.chyslivnyk.get_cardinal(101), "сто один")
        self.assertEqual(self.chyslivnyk.get_cardinal(121), "сто двадцять один")
        self.assertEqual(self.chyslivnyk.get_cardinal(200), "двісті")
        self.assertEqual(self.chyslivnyk.get_cardinal(555), "п'ятсот п'ятдесят п'ять")
        self.assertEqual(self.chyslivnyk.get_cardinal(999), "дев'ятсот дев'яносто дев'ять")

    def test_cardinal_thousands(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(1000), "тисяча")
        self.assertEqual(self.chyslivnyk.get_cardinal(1001), "одна тисяча один")
        self.assertEqual(self.chyslivnyk.get_cardinal(2000), "дві тисячі")
        self.assertEqual(self.chyslivnyk.get_cardinal(3000), "три тисячі")
        self.assertEqual(self.chyslivnyk.get_cardinal(5000), "п'ять тисяч")
        self.assertEqual(self.chyslivnyk.get_cardinal(21000), "двадцять одна тисяча")
        self.assertEqual(self.chyslivnyk.get_cardinal(12345), "дванадцять тисяч триста сорок п'ять")

    def test_cardinal_millions(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(1000000), "мільйон")
        self.assertEqual(self.chyslivnyk.get_cardinal(2000000), "два мільйони")
        self.assertEqual(self.chyslivnyk.get_cardinal(5000000), "п'ять мільйонів")
        self.assertEqual(self.chyslivnyk.get_cardinal(1000001), "один мільйон один")
        self.assertEqual(self.chyslivnyk.get_cardinal(21000000), "двадцять один мільйон")
        self.assertEqual(self.chyslivnyk.get_cardinal(22000000), "двадцять два мільйони")
        self.assertEqual(self.chyslivnyk.get_cardinal(12345678), "дванадцять мільйонів триста сорок п'ять тисяч шістсот сімдесят вісім")

    def test_cardinal_billions(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(1000000000), "мільярд")
        self.assertEqual(self.chyslivnyk.get_cardinal(2000000000), "два мільярди")
        self.assertEqual(self.chyslivnyk.get_cardinal(5000000000), "п'ять мільярдів")
        self.assertEqual(self.chyslivnyk.get_cardinal(1000000001), "один мільярд один")

    def test_cardinal_trillions(self):
        self.assertEqual(self.chyslivnyk.get_cardinal(1000000000000), "трильйон")
        self.assertEqual(self.chyslivnyk.get_cardinal(2000000000000), "два трильйони")

    def test_cardinal_cases(self):
        # Приклади відмінювання
        self.assertEqual(self.chyslivnyk.get_cardinal(25, case=CASE_NOMINATIVE), "двадцять п'ять")
        self.assertEqual(self.chyslivnyk.get_cardinal(25, case=CASE_GENITIVE), "двадцяти п'яти")
        self.assertEqual(self.chyslivnyk.get_cardinal(25, case=CASE_DATIVE), "двадцяти п'яти")
        self.assertEqual(self.chyslivnyk.get_cardinal(25, case=CASE_ACCUSATIVE), "двадцять п'ять") # для неістот
        self.assertEqual(self.chyslivnyk.get_cardinal(25, case=CASE_INSTRUMENTAL), "двадцятьма п'ятьма")
        self.assertEqual(self.chyslivnyk.get_cardinal(25, case=CASE_LOCATIVE), "двадцяти п'яти")

        self.assertEqual(self.chyslivnyk.get_cardinal(1, case=CASE_GENITIVE, gender=GENDER_MASCULINE), "одного")
        self.assertEqual(self.chyslivnyk.get_cardinal(1, case=CASE_GENITIVE, gender=GENDER_FEMININE), "однієї")
        self.assertEqual(self.chyslivnyk.get_cardinal(1, case=CASE_INSTRUMENTAL, gender=GENDER_FEMININE), "однією")

        self.assertEqual(self.chyslivnyk.get_cardinal(40, case=CASE_GENITIVE), "сорока")
        self.assertEqual(self.chyslivnyk.get_cardinal(90, case=CASE_INSTRUMENTAL), "дев'яноста")
        self.assertEqual(self.chyslivnyk.get_cardinal(100, case=CASE_LOCATIVE), "ста")
        self.assertEqual(self.chyslivnyk.get_cardinal(200, case=CASE_DATIVE), "двомстам")
        self.assertEqual(self.chyslivnyk.get_cardinal(700, case=CASE_INSTRUMENTAL), "сімомастами")

    def test_cardinal_exceptions(self):
        with self.assertRaises(TypeError):
            self.chyslivnyk.get_cardinal(2.5)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_cardinal(-5)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_cardinal(1, case="неіснуючий")

    # --- Тести для get_collective (збірні кількісні) ---
    def test_collective_basic(self):
        self.assertEqual(self.chyslivnyk.get_collective(2), "двоє")
        self.assertEqual(self.chyslivnyk.get_collective(3), "троє")
        self.assertEqual(self.chyslivnyk.get_collective(5), "п'ятеро")
        self.assertEqual(self.chyslivnyk.get_collective(10), "десятеро")

    def test_collective_cases(self):
        self.assertEqual(self.chyslivnyk.get_collective(2, case=CASE_GENITIVE), "двох")
        self.assertEqual(self.chyslivnyk.get_collective(3, case=CASE_INSTRUMENTAL), "трьома")
        self.assertEqual(self.chyslivnyk.get_collective(7, case=CASE_DATIVE), "сімом")

    def test_collective_exceptions(self):
        with self.assertRaises(TypeError):
            self.chyslivnyk.get_collective(2.0)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_collective(1) # Поза діапазоном
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_collective(11) # Поза діапазоном
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_collective(2, case="неіснуючий")

    # --- Тести для get_fractional (дробові) ---
    def test_fractional_basic(self):
        self.assertEqual(self.chyslivnyk.get_fractional(1, 2), "одна друга")
        self.assertEqual(self.chyslivnyk.get_fractional(2, 3), "дві третіх")
        self.assertEqual(self.chyslivnyk.get_fractional(3, 4), "три четвертих")
        self.assertEqual(self.chyslivnyk.get_fractional(5, 100), "п'ять сотих")
        self.assertEqual(self.chyslivnyk.get_fractional(0, 5), "нуль")

    def test_fractional_cases(self):
        self.assertEqual(self.chyslivnyk.get_fractional(1, 2, case=CASE_GENITIVE), "однієї другої")
        self.assertEqual(self.chyslivnyk.get_fractional(1, 2, case=CASE_INSTRUMENTAL), "однією другою")
        self.assertEqual(self.chyslivnyk.get_fractional(3, 4, case=CASE_DATIVE), "трьом четвертим")
        self.assertEqual(self.chyslivnyk.get_fractional(2, 5, case=CASE_GENITIVE), "двох п'ятих")
        self.assertEqual(self.chyslivnyk.get_fractional(1, 10, case=CASE_LOCATIVE), "одній десятій")


    def test_fractional_exceptions(self):
        with self.assertRaises(TypeError):
            self.chyslivnyk.get_fractional(1.0, 2)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_fractional(1, 0)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_fractional(-1, 2)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_fractional(1, 2, case="неіснуючий")

    # --- Тести для get_decimal_fractional (десяткові дроби) ---
    def test_decimal_fractional_basic(self):
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(0.5), "нуль цілих п'ять десятих")
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(3.14), "три цілих чотирнадцять сотих")
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(2.0), "два") # Ціле число як float
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(1.0), "один") # Ціле число як float

        self.assertEqual(self.chyslivnyk.get_decimal_fractional(0.0), "нуль")
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(1.25), "одна ціла двадцять п'ять сотих")

    def test_decimal_fractional_cases(self):
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(3.5, case=CASE_GENITIVE), "трьох цілих п'яти десятих")
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(1.25, case=CASE_INSTRUMENTAL), "однією цілою двадцятьма п'ятьма сотими")
        self.assertEqual(self.chyslivnyk.get_decimal_fractional(0.75, case=CASE_DATIVE), "нуль цілих сімдесяти п'яти сотим")

    def test_decimal_fractional_exceptions(self):
        with self.assertRaises(TypeError):
            self.chyslivnyk.get_decimal_fractional("0.5")
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_decimal_fractional(0.5, case="неіснуючий")

    # --- Тести для get_ordinal (порядкові) ---
    def test_ordinal_basic(self):
        self.assertEqual(self.chyslivnyk.get_ordinal(1), "перший")
        self.assertEqual(self.chyslivnyk.get_ordinal(1, gender=GENDER_FEMININE), "перша")
        self.assertEqual(self.chyslivnyk.get_ordinal(1, gender=GENDER_NEUTER), "перше")
        self.assertEqual(self.chyslivnyk.get_ordinal(1, number_type=NUMBER_PLURAL), "перші")
        self.assertEqual(self.chyslivnyk.get_ordinal(0), "нульовий")
        self.assertEqual(self.chyslivnyk.get_ordinal(2), "другий")
        self.assertEqual(self.chyslivnyk.get_ordinal(5), "п'ятий")
        self.assertEqual(self.chyslivnyk.get_ordinal(10), "десятий")
        self.assertEqual(self.chyslivnyk.get_ordinal(15), "п'ятнадцятий")
        self.assertEqual(self.chyslivnyk.get_ordinal(20), "двадцятий")
        self.assertEqual(self.chyslivnyk.get_ordinal(21), "двадцять перший")
        self.assertEqual(self.chyslivnyk.get_ordinal(21, gender=GENDER_FEMININE), "двадцять перша")
        self.assertEqual(self.chyslivnyk.get_ordinal(100), "сотий")
        self.assertEqual(self.chyslivnyk.get_ordinal(101), "сто перший") # Спрощено, має бути "сто перший"
        self.assertEqual(self.chyslivnyk.get_ordinal(121), "сто двадцять перший")
        self.assertEqual(self.chyslivnyk.get_ordinal(456888), "чотириста п'ятдесят шість тисяча вісімсот вісімдесят восьмий")

        self.assertEqual(self.chyslivnyk.get_ordinal(2000000), "два мільйонний")
        self.assertEqual(self.chyslivnyk.get_ordinal(1000000), "мільйонний")
        self.assertEqual(self.chyslivnyk.get_ordinal(1000), "тисячний")
        self.assertEqual(self.chyslivnyk.get_ordinal(1001), "одна тисяча перший") # Спрощено

    def test_ordinal_cases(self):
        self.assertEqual(self.chyslivnyk.get_ordinal(7, case=CASE_NOMINATIVE, gender=GENDER_NEUTER), "сьоме")
        self.assertEqual(self.chyslivnyk.get_ordinal(7, case=CASE_INSTRUMENTAL, gender=GENDER_NEUTER), "сьомим")
        self.assertEqual(self.chyslivnyk.get_ordinal(7, case=CASE_GENITIVE, gender=GENDER_FEMININE), "сьомої")
        self.assertEqual(self.chyslivnyk.get_ordinal(21, case=CASE_GENITIVE, gender=GENDER_MASCULINE), "двадцять першого")
        self.assertEqual(self.chyslivnyk.get_ordinal(21, case=CASE_INSTRUMENTAL, gender=GENDER_FEMININE), "двадцять першою")
        self.assertEqual(self.chyslivnyk.get_ordinal(100, case=CASE_DATIVE, gender=GENDER_FEMININE), "сотій")
        self.assertEqual(self.chyslivnyk.get_ordinal(200, case=CASE_GENITIVE, gender=GENDER_MASCULINE), "двохсотого") # Спрощено, див. коментарі в коді

    def test_ordinal_exceptions(self):
        with self.assertRaises(TypeError):
            self.chyslivnyk.get_ordinal(1.0)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_ordinal(-1)
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_ordinal(1, case="неіснуючий")
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_ordinal(1, gender="неіснуючий")
        with self.assertRaises(ValueError):
            self.chyslivnyk.get_ordinal(1, number_type="неіснуючий")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)