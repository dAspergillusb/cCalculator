from modules.windows_parameters import windows_width

# Some integer parameters
max_value_num_system = 36
min_value_num_system = 2
default_num_system = 10
width_slider = (201, 283)
num_input_width = 550
buttons_width_height = 82
main_buttons_width = 262
main_buttons_height = 42
error_with_value_width = 390
error_max_base = [310, 280]
error_max_base_window_height = 80
horizontal_spacing = 25


# Some position parameters
title_num_sys_pos = (
    [windows_width.get("numerical_system_arithmetic") // 2 - 160, 10],
    [windows_width.get("numerical_system_arithmetic") // 2 - 140, 10]
)

# Some text parameters
text_result_base: tuple[str, str] = (
    "Основание, в котором будет рассчитан результат:",
    "Witch the base result will be calculated:"
)
error_with_value: tuple[str, str] = (
    "Необходимо писать число с основанием через знак '_'.",
    "It should be value with base by '_'."
)
error_base_more_than_max: tuple[str, str] = (
    "Основание не может быть больше, чем 36!",
    "Base of number can`t be more than 36!"
)
num_sys_arith_numbers = {
    "one_arith": "1",
    "two_arith": "2",
    "three_arith": "3",
    "four_arith": "4",
    "five_arith": "5",
    "six_arith": "6",
    "seven_arith": "7",
    "eight_arith": "8",
    "nine_arith": "9",
    "dot_arith": ".",
    "zero_arith": "0",
    "plus_minus_arith": "+/-"
}
num_sys_arith_actions = {
    "enter_base": "Enter base",
    "calculate": "=",
    "erase_arith": "C",
    "delete_arith": "del",
    "bracket_open": "(",
    "bracket_close": ")",
    "plus_arith": "+",
    "minus_arith": "-",
    "divide_arith": "/",
    "multiply_arith": "x"
}
