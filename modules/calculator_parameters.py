from dearpygui.dearpygui import (
    mvKey_0,
    mvKey_1,
    mvKey_2,
    mvKey_3,
    mvKey_4,
    mvKey_5,
    mvKey_6,
    mvKey_7,
    mvKey_8,
    mvKey_9,
    mvKey_Plus,
    mvKey_Minus,
    mvKey_Multiply,
    mvKey_Divide,
    mvKey_Back,
    mvKey_Return,
    mvKey_NumPad0,
    mvKey_NumPad1,
    mvKey_NumPad2,
    mvKey_NumPad3,
    mvKey_NumPad4,
    mvKey_NumPad5,
    mvKey_NumPad6,
    mvKey_NumPad7,
    mvKey_NumPad8,
    mvKey_NumPad9,
    mvKey_Add,
    mvKey_Subtract,
    mvKey_Slash,
    mvKey_Delete,
    mvKey_Period,
    mvKey_Decimal,
    mvKey_Open_Brace,
    mvKey_Close_Brace
)
from modules.windows_parameters import windows_height

# Some int parameters
title_pos = (
    [windows_height.get("calculator") // 2 - 28, 10],
    [windows_height.get("calculator") // 2, 10]
)
error_zero_div_width = (180, 200)
error_factorial_width = (160, 130)
error_height = 80
error_button_width = 76
input_text_width = 492
radians_degrees_combo_width = 90
rounded_combo_width = 50
button_width = 60
additional_button_width = button_width * 3 + 16
button_height = 30
button_main_menu_exit_width = 242
input_number_root_width = [50, 84]
spacing_with_value_types_options = [9, 52]
delta_for_root_button = 8
radical_x_window_width = 180
radical_x_window_height = 40
horizontal_spacing_for_buttons_blocks = 20
old_operations_input_text_height = 90


# Errors messages
mistake = ("Ошибка!", "Error!")
error_zero_division = ("Нельзя делить на ноль!", "There is no division by zero!")
error_factorial = ("Отрицательно число!", "Value is negative!")

# Text labels
rounded_for: list[str] = [
    "Знаков после запятой:",
    "Decimal places:"
]
root_titles: list[tuple[str, str]] = [
    ("Число:", "Number:"),
    ("Степень корня:", "Root value:"),
    ("Отмена", "Cancel")
]
is_rational_fractions = [
    "Рациональные дроби",
    "Rational fractions"
]

# Selectable items
trigonometry_values_list: list[tuple[str, str, str]] = [
    ("Радианы", "Градусы", "Грады"),
    ("Radians", "Degrees", "Grads")
]
round_for_digits_list: list[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14"
]

# Buttons dicts
first_block_buttons: dict[str:str] = {
    "erase": "C",
    "delete": "Del",
    "parenthesis": "( )",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "dot": ".",
    "zero": "0",
    "plus-minus": "+/-"
}
second_block_buttons: dict[str:str] = {
    "minus": "-",
    "plus": "+",
    "multiply": "*",
    "divide": "/",
    "result": "="
}
third_block_buttons: dict[str:str] = {
    "additional_functions": ("Доп. функции", "Additional functions"),
    "reverse_num": "1 / x",
    "sin": "sin(x)",
    "rad2": "²√x",
    "factorial": "!",
    "cos": "cos(x)",
    "rad3": "³√x",
    "percentage": "%",
    "tan": "tan(x)",
    "powerXY": "xⁿ",
    "log₁₀": "lg(x)",
    "cot": "cot(x)",
    "square": "x²"
}
shift_block_buttons = {
    "radX": "ⁿ√x",
    "log₂": "log₂(x)",
    "ln": "ln(x)",
    "sinh": "sinh(x)",
    "cosh": "cosh(x)",
    "tanh": "tanh(x)",
    "asin": "asin(x)",
    "acos": "acos(x)",
    "atan": "atan(x)",
    "asinh": "asinh(x)",
    "acosh": "acosh(x)",
    "atanh": "atanh(x)",

}
key_handler: dict[str: int] = {
    "zero_0": mvKey_0,
    "zero_numpad": mvKey_NumPad0,
    "one_1": mvKey_1,
    "one_numpad": mvKey_NumPad1,
    "two_2": mvKey_2,
    "two_numpad": mvKey_NumPad2,
    "three_3": mvKey_3,
    "three_numpad": mvKey_NumPad3,
    "four_4": mvKey_4,
    "four_numpad": mvKey_NumPad4,
    "five_5": mvKey_5,
    "five_numpad": mvKey_NumPad5,
    "six_6": mvKey_6,
    "six_numpad": mvKey_NumPad6,
    "seven_7": mvKey_7,
    "seven_numpad": mvKey_NumPad7,
    "eight_8": mvKey_8,
    "eight_numpad": mvKey_NumPad8,
    "nine_9": mvKey_9,
    "nine_numpad": mvKey_NumPad9,
    "dot_decimal": mvKey_Decimal,
    "dot_period": mvKey_Period,
    "plus_plus": mvKey_Plus,
    "plus_add": mvKey_Add,
    "minus_minus": mvKey_Minus,
    "minus_subtract": mvKey_Subtract,
    "multiply_multiply": mvKey_Multiply,
    "divide_divide": mvKey_Divide,
    "divide_slash": mvKey_Slash,
    "delete_delete": mvKey_Delete,
    "erase_back": mvKey_Back,
    "result_return": mvKey_Return,
    "parenthesis_open": mvKey_Open_Brace,
    "parenthesis_close": mvKey_Close_Brace
}
