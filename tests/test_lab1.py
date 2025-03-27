import subprocess
import pytest

INTERPRETER = 'python'


def run_script(filename, input_data=None):
    filepath = f'./tasks/hw1/{filename}'
    proc = subprocess.run(
        [INTERPRETER, filepath],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=True
    )
    return proc.stdout.strip()


class TestLab1:
    test_data = {
        'hello': [
            ([], 'Hello, world!'),
        ],
        'python_if_else': [
            ('1', 'Weird'),
            ('4', 'Not Weird'),
            ('3', 'Weird'),
            ('6','Weird'),
            ('22', 'Not Weird')
        ],
        'arithmetic_operators': [
            (['1', '2'], ['3', '-1', '2']),
            (['10', '5'], ['15', '5', '50']),
            (['1488', '1337'], ['2825', '151', '1989456'])
        ],
        'division': [
            (['1', '2'], ['0', '0.5']),
            (['1488', '80'], ['18', '18.6']),
            (['20', '5'], ['4', '4.0'])
        ],
        'loops': [
            ('3', ['0', '1', '4']),
            ('13', ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81', '100', '121', '144']),
            ('5', ['0', '1', '4', '9', '16'])
        ],
        'print_function': [
            ('5', '12345'),
            ('19', '12345678910111213141516171819'),
            ('7', '1234567')
        ],
        'second_score': [
            (['5', '2 3 6 6 5'], '5'),
            (['8', '1 4 8 8 2 5 4 4'], '5'),
            (['3', '1 2 1'], '1'),
        ],
        'nested_list': [
            (['5', 'Гарри', '37.21', 'Берри', '37.21', 'Тина', '37.2', 'Акрити', '41', 'Харш', '39'], ['Берри', 'Гарри']),
            (['3', 'Гарри', '112', 'Берри', '123', 'Тина', '112.01'], ['Тина']),
            (['4', 'Гарри', '5', 'Берри', '5', 'Тина', '4.9', 'Акрити', '5'], ['Акрити', 'Берри', 'Гарри'])
        ],
        'lists': [
            (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], ['[1, 3, 2]']),
            (['12', 'insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 
            'print', 'pop', 'reverse', 'print'], ['[6, 5, 10]', '[1, 5, 9, 10]', '[9, 5, 1]']),
            (['6', 'append 3', 'append 17', 'print', 'pop', 'remove 3', 'print'], ['[3, 17]', '[]'])
        ],
        'swap_case': [
            ('Www.MosPolytech.ru', 'wWW.mOSpOLYTECH.RU'),
            ('Pythonist 2', 'pYTHONIST 2'),
            ('snake_case better then camelCase', 'SNAKE_CASE BETTER THEN CAMELcASE'),
            ('Wh4T 1F 1 uS3 s0M3 nuMb3Rs?', 'wH4t 1f 1 Us3 S0m3 NUmB3rS?')
        ],
        'split_and_join': [
            ('this is a string', 'this-is-a-string'),
            ('test this code', 'test-this-code'),
            ('ve nom ve nom ve nom', 've-nom-ve-nom-ve-nom')
        ],
        'max_word': [
            ([], ['сосредоточенности', 'сосредоточенности']),
        ],
        'price_sum': [
            ([], ['6842.84', '5891.06', '6810.90'])
        ],
        'anagram': [
            (['просветитель', 'терпеливость'], 'YES'),
            (['краснодар', 'покраснение'], 'NO'),
            (['антиквар ', 'травинка'], 'YES')
        ],
        'metro': [
            (['3', '10 20', '5 15', '2 12', '13'], '2'),
            (['5', '10 20', '5 15', '2 12', '13 21', '124 125', '124'], '1'),
            (['2', '5 15', '2 12', '16'], '0')
        ],
        'minion_game': [
            ('BANANA', 'Стюарт 12'),
            ('UNICODE', 'Кевин 16'),
            ('KEVIN', 'Стюарт 9')
        ],
        'is_leap': [
            ('2000', 'True'),
            ('1800', 'False'),
            ('1900', 'False'),
            ('2400', 'True'),
            ('2100', 'False'),
            ('2200', 'False'),
            ('2300', 'False'),
            ('2500', 'False')
        ],
        'happiness': [
            (['3 2', '1 5 3', '3 1', '5 7'], '1'),
            (['3 3', '1 3 5', '4 5 6', '1 2 3'], '-1'),
            (['6 2', '11 2 51 3 21 4', '2 51', '11 21'], '0')
        ],
        'pirate_ship': [
            (['10 3', 'Сундук 25 375', 'Самоцвет 5 100', 'Серебро 15 100'], 
            ['Серебро 10.00 66.67', 'Самоцвет 5.00 100.00', 'Сундук 10.00 150.00']),
            (['25 4', 'Серебро 15 100', 'Сундук 25 375', 'Самоцвет 5 100', 'Золото 50 500'], 
            ['Серебро 15.00 100.00', 'Самоцвет 5.00 100.00', 'Золото 25.00 250.00', 'Сундук 25.00 375.00']),
            (['10 2', 'Сундук 25 375', 'Золото 50 500'], ['Золото 10.00 100.00', 'Сундук 10.00 150.00',])
        ],
        'matrix_mult': [
            (['3', '1 2 3', '4 5 6', '7 8 9', '9 8 7', '6 5 4', '3 2 1'], ['30 24 18', '84 69 54', '138 114 90']),
            (['4', '1 4 8 8', '1 3 3 7', '5 2 5 2', '4 2 4 2', '1 2 3 4', '4 3 2 1', '5 6 7 8', '8 7 6 5'], 
            ['121 118 115 112', '84 78 72 66', '54 60 66 72', '48 52 56 60']),
            (['3', '1 2 3', '4 5 6', '7 8 9', '1 0 0', '0 1 0', '0 0 1'], ['1 2 3', '4 5 6', '7 8 9'])
        ]
    }

    @pytest.mark.parametrize('input_data, expected', test_data['hello'])
    def test_hello_world(self, input_data, expected):
        assert run_script('hello.py', input_data) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['python_if_else'])
    def test_python_if_else(self, input_data, expected):
        assert run_script('python_if_else.py', [input_data]) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['arithmetic_operators'])
    def test_arithmetic_operators(self, input_data, expected):
        assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['division'])
    def test_division(self, input_data, expected):
        assert run_script('division.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['loops'])
    def test_loops(self, input_data, expected):
        assert run_script('loops.py', [input_data]).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['print_function'])
    def test_print_function(self, input_data, expected):
        assert run_script('print_function.py', [input_data]) == expected
        
    @pytest.mark.parametrize('input_data, expected', test_data['second_score'])
    def test_second_score(self, input_data, expected):
        assert run_script('second_score.py', input_data) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['nested_list'])
    def test_nested_list(self, input_data, expected):
        assert run_script('nested_list.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['lists'])
    def test_lists(self, input_data, expected):
        assert run_script('lists.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['swap_case'])
    def test_swap_case(self, input_data, expected):
        assert run_script('swap_case.py', [input_data]) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['split_and_join'])
    def test_split_and_join(self, input_data, expected):
        assert run_script('split_and_join.py', [input_data]) == expected
    
    @pytest.mark.parametrize('input_data, expected', test_data['max_word'])
    def test_max_word(self, input_data, expected):
        assert run_script('max_word.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['price_sum'])
    def test_price_sum(self, input_data, expected):
        assert run_script('price_sum.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['anagram'])
    def test_anagram(self, input_data, expected):
        assert run_script('anagram.py', input_data) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['metro'])
    def test_metro(self, input_data, expected):
        assert run_script('metro.py', input_data) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['minion_game'])
    def test_minion_game(self, input_data, expected):
        assert run_script('minion_game.py', [input_data]) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['is_leap'])
    def test_is_leap(self, input_data, expected):
        assert run_script('is_leap.py', [input_data]) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['happiness'])
    def test_happiness(self, input_data, expected):
        assert run_script('happiness.py', input_data) == expected

    @pytest.mark.parametrize('input_data, expected', test_data['pirate_ship'])
    def test_pirate_ship(self, input_data, expected):
        assert run_script('pirate_ship.py', input_data).split('\n') == expected

    @pytest.mark.parametrize('input_data, expected', test_data['matrix_mult'])
    def test_matrix_mult(self, input_data, expected):
        assert run_script('matrix_mult.py', input_data).split('\n') == expected
