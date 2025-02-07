from modules.windows_parameters import windows_width


# Some integer parameters
plot_width = 780
plot_height = 600
func_y_input_text_width = 408
build_der_width = 268
build_der_height = 48
main_buttons_width = 385

title_deriv_pos = (
    [windows_width.get("derivative") // 2 - 30, 10],
    [windows_width.get("derivative") // 2 - 50, 10]
)
func_y = (
    "Функция y = ",
    "Function y ="
)
func_y_der = (
    "Функция y' =",
    "Function y'="
)
build_der = (
    "Взять производную",
    "Build Derivative "
)
