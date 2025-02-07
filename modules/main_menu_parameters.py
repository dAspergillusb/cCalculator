from modules.windows_parameters import windows_height, windows_width

# Some int parameters
start_tag_num = 0
delta_tag = 1
start_pos_y = 50
delta_pos_y = 30
center_text_title = (
    [windows_width.get("main_menu") // 2 - 70, 10],
    [windows_width.get("main_menu") // 2 - 50, 10]
)
buttons_width = 240

main_menu_buttons = {
    "go_to_calculator": ("Калькулятор", "Calculator"),
    "go_to_numerical_system": ("Системы счисления", "Numeral systems"),
    "go_to_numerical_system_arithmetic": ("Системы счисления арифметика", "Numeral systems - arithmetic"),
    "go_to_graphics": ("Построение графиков", "Build graphs"),
    "go_to_derivative": ("Производные", "Derivatives"),
    "close": ("Выйти из программы", "Exit from cCalc")
}
main_menu_buttons_tags = (
    "calc",
    "num_sys",
    "num_sys_ariph",
    "grphs",
    "deriv",
    "exit"
)
