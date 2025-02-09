import pytest
from StringUtils import StringUtils
#Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст/Позитивные
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "Hello"),
        ("привет", "Привет")
    ]
)
def test_capitilize(input_string, expected_output):
    processor = StringUtils()
    assert processor.capitilize(input_string) == expected_output

#Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст/Негативные
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hEllo", "HEllo"),
        ("", "")
    ]
)
def test_capitilize(input_string, expected_output):
    processor = StringUtils()
    assert processor.capitilize(input_string) == expected_output

#Принимает на вход текст и удаляет пробелы в начале, если они есть/ Позитивные
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (" hello", "Hello"),
        (" привет", "Привет")
    ]
)
def test_trim(input_string, expected_output):
    processor = StringUtils()
    assert processor.trim(input_string) == expected_output

#Принимает на вход текст и удаляет пробелы в начале, если они есть/ Негативные
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (None, TypeError),
        ([], TypeError)
    ]
)
def test_trim(input_string, expected_output):
    processor = StringUtils()
    assert processor.trim(input_string) == expected_output

#Принимает на вход текст с разделителем и возвращает список строк.Позитивные
@pytest.mark.parametrize(
    "input_string, delimiter, expected_output",
    [
        ("Name, Class, Age", ["Name", "Class", "Age"]),
        ("122:123:124", ":" ["122", "123", "124"]),
         ("Учеба скайпро", " ", ["Учеба", "скайпро"])
    ]
)
def test_to_list(input_string, delimiter, expected_output):
    processor = StringUtils()
    assert processor.to_list(input_string, delimiter) == expected_output

#Принимает на вход текст с разделителем и возвращает список строк.Негативные
@pytest.mark.parametrize(
    "input_string, delimiter, expected_output",
    [
        ("Name", " ", "Name"),
        ("122 123", "122", "123")
    ]
)
def test_to_list(input_string, delimiter, expected_output):
    processor = StringUtils()
    assert processor.to_list(input_string, delimiter) == expected_output

#Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n. Позитивные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Severus", "S", True),  
        ("Class123", "1", True),  
        ("Учеба", "У", True)
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output

#Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n. негативные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("", "a", False), 
        ("abc123", "8", False),
        ("Тесты в школе", "F", False)
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output
#Удаляет все подстроки из переданной строки \Позитивные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Работа", "р", "абота"), 
        ("Учат в школе", "в", "Учат школе"),
        ("Станция 234", "Станция", "234")
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output
#Удаляет все подстроки из переданной строки \Негативные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Работа учителем", "", "Работа учителем"), 
        (None, "в", TypeError),
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output
#Возвращает `True`, если строка начинается с заданного символа и `False` - если нет/ Позитивные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Работа", "Р", True), 
        ("Where", "w", False),
        ("123", "1", True)
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output
#Возвращает `True`, если строка начинается с заданного символа и `False` - если нет/Негативные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        (None, "G", TypeError), 
        ("Rich", None, TypeError),
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output
#Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет/ Позитивные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        ("Свет в окошке", "е", True), 
        ("Rich", "H", False),
        ("12345", "5", True)
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output

#Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет/ Негативные
@pytest.mark.parametrize(
    "input_string, symbol, expected_output",
    [
        (None, "G", TypeError), 
        ("RichREsy", None, TypeError),
    ]
)
def test_contains(input_string, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string, symbol) == expected_output
#Возвращает `True`, если строка пустая и `False` - если нет/ Позитивные
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("  ", True), 
        ("RichREsy", False),
    ]
)
def test_contains(input_string, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string) == expected_output

#Возвращает `True`, если строка пустая и `False` - если нет/ Негативные
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (None, TypeError), 
    ]
)
def test_contains(input_string, expected_output):
    processor = StringUtils()
    assert processor.contains(input_string) == expected_output
#Преобразует список элементов в строку с указанным разделителем/ Позитивные
@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
        ([1, 2, 3], ", ", "1, 2, 3"),
        (["Один", "Два"], ", ", "Один, Два"),   
        (["Шило", "Мыло"], "-", "Шило-Мыло"),     
        ([], ", ", ""),                         
        ([1], ", ", "1")                      
    
    ]
)
def test_list_to_string(input_list, joiner, expected_output):
    processor = StringUtils()
    assert processor.list_to_string(input_list, joiner) == expected_output
#Преобразует список элементов в строку с указанным разделителем/ Негативные
@pytest.mark.parametrize(
    "input_list, joiner, expected_output",
    [
       (None, ", ", TypeError),              
        (["Светит", "Солнце"], None, TypeError)                     
    ]
)
def test_list_to_string(input_list, joiner, expected_output):
    processor = StringUtils()
    assert processor.list_to_string(input_list, joiner) == expected_output