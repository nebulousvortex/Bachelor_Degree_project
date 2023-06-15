import unittest

from Main import convert_date, app, toggle_modal_1, toggle_modal_2, toggle_modal_3, \
    toggle_modal_4, toggle_modal_5, get_attributes

# app = import_app("app")

""" Тестирование обратного вызова

В данном методе происходит тестирование метода convert_date

"""


def test_convert_date():
    test_date = "2022.12.12"
    test_start = "00:00:00"
    test_end = "16:00:00"
    expected_output = "2022.12.12  00:00:00  16:00:00"

    response = convert_date(test_date, test_start, test_end)

    assert response == expected_output


class TestCallbacks(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.value = 'Turbine_1'
        self.n_clicks = 1
        self.objects = 'Turbine_1'
        self.attribute = 'Time'
        self.date = '22.12.12'
        self.start = '00:00:00'
        self.end = '01:00:00'
        pass

    def tearDown(self):
        self.app = None
        pass

    def test_update_atr(self):
        # установка тестовых параметров
        value = self.value
        # вызов функции callback
        result1, result2 = get_attributes(value)
        # проверка результатов запросов к базе данных
        self.assertEqual(result1, value)
        self.assertIsNotNone(result2)

    def test_get_attributes(self):
        # установка тестовых параметров
        value = self.value
        # вызов функции callback
        result1, result2 = get_attributes(value)
        # проверка результатов запросов к базе данных
        self.assertEqual(result1, value)
        self.assertIsNotNone(result2)

    def test_toggle_modal_1(self):
        # установка тестовых параметров
        n0, n1, is_open = 1, 0, True
        # вызов функции callback
        result = toggle_modal_1(n0, n1, is_open)
        # проверка соответствующего результата
        self.assertFalse(result)
        # установка тестовых параметров
        n0, n1, is_open = 0, 1, False
        # вызов функции callback
        result = toggle_modal_1(n0, n1, is_open)
        # проверка соответствующего результата
        self.assertTrue(result)

    def test_toggle_modal_2(self):
        # установка тестовых параметров
        n1, n2, is_open = 1, 0, True
        # вызов функции callback
        result = toggle_modal_2(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertFalse(result)
        # установка тестовых параметров
        n1, n2, is_open = 0, 1, False
        # вызов функции callback
        result = toggle_modal_2(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertTrue(result)

    def test_toggle_modal_3(self):
        # установка тестовых параметров
        n1, n2, is_open = 1, 0, True
        # вызов функции callback
        result = toggle_modal_3(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertFalse(result)
        # установка тестовых параметров
        n1, n2, is_open = 0, 1, False
        # вызов функции callback
        result = toggle_modal_3(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertTrue(result)

    def test_toggle_modal_4(self):
        # установка тестовых параметров
        n1, n2, is_open = 1, 0, True
        # вызов функции callback
        result = toggle_modal_4(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertFalse(result)
        # установка тестовых параметров
        n1, n2, is_open = 0, 1, False
        # вызов функции callback
        result = toggle_modal_4(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertTrue(result)

    def test_toggle_modal_5(self):
        # установка тестовых параметров
        n1, n2, is_open = 1, 0, True
        # вызов функции callback
        result = toggle_modal_5(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertFalse(result)
        # установка тестовых параметров
        n1, n2, is_open = 0, 1, False
        # вызов функции callback
        result = toggle_modal_5(n1, n2, is_open)
        # проверка соответствующего результата
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
    test_convert_date()
