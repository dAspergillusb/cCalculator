from modules.windows_parameters import windows_width


# Some functions
def error_wrong_base(base: int) -> tuple[str, str]:
    return (
        f"Данное число в системе счисления с основанием {base} не существует!",
        f"There is no such number with base {base}!"
    )


# Some int parameters
index_char_a_upper = 65
index_char_z_upper = 90
delta_for_num = 55
bases_default_value = 2
bases_min_value = 2
bases_max_value = 36
menu_buttons_width = 205
error_empty_num_width = 220
error_wrong_base_width = (475, 265)
error_window_height = 100
error_window_button_width = 76
input_text_sliders_width = 420

# Error messages
number = (
    "Число",
    "Number"
)
number_base = (
    "Основание числа",
    "Number base"
)
result_number_base = (
    "Основание конечного числа",
    "Result number base"
)
result_number = (
    "Результат",
    "Result number"
)
mistake = (
    "Ошибка!",
    "Error!"
)
error_empty_num = (
    "Введите число для перевода",
    "Insert the number to convert"
)
error_empty_num_return = (
    "Нечего переводить!",
    "Nothing to convert!"
)
title_num_sys_pos = (
    [windows_width.get("numerical_system") // 2 - 100, 10],
    [windows_width.get("numerical_system") // 2 - 80, 10]
)
num_input_text_pos = [
    windows_width.get("numerical_system") // 2 - 112,
    42
]
base_from_slider_pos = [
    windows_width.get("numerical_system") // 2 - 112,
    72
]
base_to_slider_pos = [
    windows_width.get("numerical_system") // 2 - 112,
    98
]
num_to_pos = [
    windows_width.get("numerical_system") // 2 - 112,
    124
]
