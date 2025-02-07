from typing import Never
from dearpygui.dearpygui import (
    window,
    group,
    bind_item_font,
    add_input_text,
    add_text,
    add_button,
    add_slider_int,
    get_value,
    set_value,
    stop_dearpygui,
    configure_item,
    bind_item_theme,
)
from modules.ErrorMessage import ErrorMessage
from modules.Types import MainMenu, Themes, FontRegistry
from modules.windows_parameters import windows_height, windows_width
from modules.main_config import TITLES
from modules.num_sys_parameters import (
    delta_for_num,
    index_char_a_upper,
    index_char_z_upper,
    error_wrong_base,
    error_wrong_base_width,
    error_window_height,
    error_window_button_width
)
from modules.num_sys_arith_parameters import (
    num_sys_arith_numbers,
    num_sys_arith_actions, error_base_more_than_max, error_max_base, error_max_base_window_height,
)
from modules.num_sys_arith_parameters import (
    max_value_num_system,
    min_value_num_system,
    default_num_system,
    width_slider,
    title_num_sys_pos,
    text_result_base,
    buttons_width_height,
    main_buttons_width,
    main_buttons_height,
    error_with_value,
    error_with_value_width,
    horizontal_spacing,
)
from modules.calculator_parameters import (
    error_zero_div_width,
    error_zero_division,
    error_height,
    error_button_width,
    mistake
)
from modules.num_sys_arith_parameters import num_input_width
from modules.font_chars import (
    CHARS_DICT_SUBSCRIPT
)


class NumericalSystemArithmetic:

    def __init__(self,
                 lang: int,
                 main_menu: MainMenu,
                 font_header: FontRegistry.get_font_header,
                 font_num_sys_arith: FontRegistry.get_font_calculator,
                 themes: Themes
                 ):
        self.main_menu = main_menu
        self.result_ok = True
        self.shift_lock = False
        self.lang = lang
        self.shifted_button = themes.get_shifted_theme()
        self.default_button = themes.get_default_button_theme()
        self.disabled_button = themes.get_disabled_button_theme()
        self.dic_bigger_than_10 = {index - delta_for_num: chr(index) for index in range(
            index_char_a_upper,
            index_char_z_upper + 1
        )}
        self.chars_dict_subscript_reverse_key_value = {
            value: key for key, value in CHARS_DICT_SUBSCRIPT.items()
        }
        with window(
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                tag="numerical_system_arithmetic",
                width=windows_width.get("numerical_system_arithmetic"),
                height=windows_height.get("numerical_system_arithmetic"),
                show=False
        ) as self.numerical_system_arithmetic:
            with group(horizontal=True):
                title_num_sys = add_text(
                    default_value=TITLES["num_sys_arith"][self.lang],
                    pos=title_num_sys_pos[self.lang]
                )
                bind_item_font(title_num_sys, font_header)
            with group():
                self.num = add_input_text(width=num_input_width)
                bind_item_font(self.num, font_num_sys_arith)
            with group(horizontal=True):
                add_text(text_result_base[self.lang])
                self.base2 = add_slider_int(
                    default_value=default_num_system,
                    min_value=min_value_num_system,
                    max_value=max_value_num_system,
                    width=width_slider[self.lang]
                )
            self.functions_num_sys_arith = {
                "plus_arith": self.plus,
                "minus_arith": self.minus,
                "bracket_open": self.bracket_open,
                "plus_minus_arith": self.plus_minus,
                "erase_arith": self.erase,
                "divide_arith": self.divide,
                "multiply_arith": self.multiply,
                "bracket_close": self.bracket_close,
                "delete_arith": self.delete,
                "calculate": self._get_equation,
                "dot_arith": self.dot,
                "enter_base": self._enter_base
            }
            self.buttons_disabled_after_shift_lock: tuple[str, ...] = (
                "plus_arith",
                "minus_arith",
                "bracket_open",
                "plus_minus_arith",
                "divide_arith",
                "multiply_arith",
                "bracket_close",
                "erase_arith",
                "calculate",
                "dot_arith"
            )
            with group(horizontal_spacing=horizontal_spacing, horizontal=True):
                with group():
                    index = 0
                    number_buttons = tuple(num_sys_arith_numbers.items())
                    while index < len(num_sys_arith_numbers):
                        with group(horizontal=True):
                            for tag, label in number_buttons[index:index + 3]:
                                add_button(
                                    label=label,
                                    tag=tag,
                                    callback=self._return_number,
                                    width=buttons_width_height,
                                    height=buttons_width_height
                                )
                        index += 3
                with group():
                    index = 0
                    action_buttons = tuple(num_sys_arith_actions.items())
                    while index < 4:
                        with group(horizontal=True):
                            tag = action_buttons[index][0]
                            label = action_buttons[index][1]
                            add_button(
                                label=label,
                                tag=tag,
                                callback=self.functions_num_sys_arith[tag],
                                width=(buttons_width_height + 4) * 2,
                                height=buttons_width_height
                            )
                            tag = action_buttons[index + 1][0]
                            label = action_buttons[index + 1][1]
                            add_button(
                                label=label,
                                tag=tag,
                                callback=self.functions_num_sys_arith[tag],
                                width=buttons_width_height,
                                height=buttons_width_height
                            )
                        index += 2
                    while index < len(num_sys_arith_actions):
                        with group(horizontal=True):
                            for tag, label in action_buttons[index:index + 3]:
                                add_button(
                                    label=label,
                                    tag=tag,
                                    callback=self.functions_num_sys_arith[tag],
                                    width=buttons_width_height,
                                    height=buttons_width_height
                                )
                        index += 3
            with group(horizontal_spacing=horizontal_spacing, horizontal=True):
                add_button(
                    label=TITLES["main_menu"][self.lang],
                    callback=main_menu.go_to_main_menu,
                    width=main_buttons_width,
                    height=main_buttons_height
                )
                add_button(
                    label=TITLES["exit"][self.lang],
                    callback=self.close,
                    width=main_buttons_width,
                    height=main_buttons_height
                )

    def get_numerical_system_arithmetic(self) -> window:
        return self.numerical_system_arithmetic

    @staticmethod
    def close() -> Never:
        stop_dearpygui()

    def _enter_base(self) -> None:
        if self.shift_lock:
            self._change_buttons_to_nums()
        else:
            self._change_buttons_to_num_bases()
        self.shift_lock = not self.shift_lock

    def _change_buttons_to_num_bases(self) -> None:
        bind_item_theme("enter_base", self.shifted_button)
        for button in self.buttons_disabled_after_shift_lock:
            bind_item_theme(button, self.disabled_button)
            configure_item(button, callback=self._disabled_button)
        for num_button in num_sys_arith_numbers:
            if num_button not in ["dot_arith", "plus_minus_arith"]:
                configure_item(
                    num_button,
                    label=self.chars_dict_subscript_reverse_key_value[num_sys_arith_numbers[num_button]]
                )

    def _change_buttons_to_nums(self) -> None:
        bind_item_theme("enter_base", self.default_button)
        for button in self.buttons_disabled_after_shift_lock:
            bind_item_theme(button, self.default_button)
            configure_item(button, callback=self.functions_num_sys_arith.get(button))
        for num_button in num_sys_arith_numbers:
            if num_button not in ["dot_arith", "plus_minus_arith"]:
                configure_item(
                    num_button,
                    label=num_sys_arith_numbers[num_button]
                )

    def _check_if_shifted(self, char: str) -> set_value:
        if self.result_ok:
            set_value(self.num, "")
            self.result_ok = False
        if self.shift_lock:
            return self._insert_numeral_system(char=char)
        return self._insert_num(char=char)

    def _insert_num(self, char: str) -> None:
        num = get_value(self.num)
        num += char
        return set_value(self.num, num)

    def _insert_action(self, char: str) -> set_value:
        num = get_value(self.num)
        if not num:
            return set_value(self.num, '')
        if num[-1] == ' ':
            return ''
        num += f' {char} '
        set_value(self.num, num)

    def _insert_numeral_system(self, char: str) -> str | None:
        num = get_value(self.num)
        if not num:
            return ""
        if len(num) > 1:
            if num[-2] in ["+", "-", "/", "*"]:
                return ""
        base = self.chars_dict_subscript_reverse_key_value[char]
        set_value(self.num, num + base)

    @staticmethod
    def _disabled_button() -> None:
        return None

    def _return_number(self, tag: str) -> None:
        if tag == "dot_arith":
            return self.dot()
        elif tag == "plus_minus_arith":
            return self.plus_minus()
        label = num_sys_arith_numbers[tag]
        return self._check_if_shifted(label)

    def plus(self) -> _insert_action:
        return self._insert_action("+")

    def minus(self) -> _insert_action:
        return self._insert_action("-")

    def divide(self) -> _insert_action:
        return self._insert_action("/")

    def multiply(self) -> _insert_action:
        return self._insert_action("*")

    def dot(self) -> str | None:
        if get_value(self.num)[-1] == '.':
            return ''
        num = get_value(self.num)
        num += '.'
        set_value(self.num, num)

    def plus_minus(self) -> set_value:
        num = get_value(self.num)
        if num == '':
            return set_value(self.num, '')
        if num.isdecimal():
            return set_value(self.num, '-' + num)
        elif get_value(self.num)[0] == '-':
            return set_value(self.num, num[1:])

    def _get_equation(self) -> str | None:
        equation: list[str, ...] = get_value(self.num).split()
        self.result_ok = True
        if not len(equation):
            return ""
        if len(equation) == 1:
            result = self._calculate_number_to_integer(equation=equation[0])
            result_base_to = self._convert_to_base2(eval(result), get_value(self.base2))
            return self._insert_result(result_base_to)
        self._translate_equation_to_integer(equation=equation)

    def _translate_equation_to_integer(self, equation: list[str, ...]) -> str | None:
        result = self._transform_values_to_integers(equation=equation)
        try:
            result = self._convert_to_base2(eval(result), get_value(self.base2))
        except ZeroDivisionError:
            ErrorMessage(
                title=mistake[self.lang],
                message=error_zero_division[self.lang],
                width=error_zero_div_width[self.lang],
                height=error_height,
                button_width=error_button_width
            )
            return "0"
        return self._insert_result(result=result)

    def _insert_result(self, result: str) -> None:
        return set_value(self.num, result)

    def _transform_values_to_integers(self, equation: list[str, ...]) -> str:
        integers_equation: str = ""
        bracket_close: bool = False
        for eq in range(len(equation)):
            if equation[eq].find("(") >= 0:
                integers_equation += equation[eq][0:1]
                equation[eq] = equation[eq][1:]
            elif equation[eq].find(")") >= 0:
                equation[eq] = equation[eq][:-1]
                bracket_close = True
            if bracket_close:
                integers_equation += self._calculate_number_to_integer(equation[eq]) + ")"
                bracket_close = False
            elif eq % 2 == 0:
                integers_equation += self._calculate_number_to_integer(equation[eq])
            else:
                integers_equation += " " + equation[eq] + " "
        return integers_equation

    def _calculate_number_to_integer(self, equation: str) -> str:
        equation = equation if equation.isdecimal() else self._equation_with_underscore(equation)
        try:
            num, base = equation.split("_")  # TODO
        except ValueError:
            num, base = equation, "10"
        result = self._check_at_floating(num, int(base))
        return result

    def _equation_with_underscore(self, num_with_base: str) -> str | ErrorMessage:
        if num_with_base[-2].isdecimal() or num_with_base[-2] in self.dic_bigger_than_10.values():
            return f"{num_with_base[:-1]}_{CHARS_DICT_SUBSCRIPT[num_with_base[-1]]}"
        elif num_with_base[-3].isdecimal() or num_with_base[-3] in self.dic_bigger_than_10.values():
            base = f"{CHARS_DICT_SUBSCRIPT[num_with_base[-2]]}{CHARS_DICT_SUBSCRIPT[num_with_base[-1]]}"
            if int(base) > 36:
                return ErrorMessage(
                    title=mistake[self.lang],
                    message=error_base_more_than_max[self.lang],
                    width=error_max_base[self.lang],
                    height=error_max_base_window_height,
                    button_width=error_button_width
                )
            return f"{num_with_base[:-2]}_{base}"
        else:
            return ErrorMessage(
                title=mistake[self.lang],
                message=error_base_more_than_max[self.lang],
                width=error_max_base[self.lang],
                height=error_max_base_window_height,
                button_width=error_button_width
            )

    def bracket_open(self) -> str | None:
        num = get_value(self.num)
        if num.count("(") > num.count(")"):
            return ""
        num += "("
        set_value(self.num, num)

    def bracket_close(self) -> str | None:
        num = get_value(self.num)
        if num.count("(") == num.count(")"):
            return ""
        num += ")"
        set_value(self.num, num)

    def delete(self) -> None:
        set_value(self.num, get_value(self.num)[:-1])

    def erase(self) -> None:
        set_value(self.num, "")

    def _check_at_floating(self, n: str, base: int) -> str:
        lst_number_parts = n.split(".")

        if len(lst_number_parts) == 1:
            int_part = self._convert_int_part_to_decimal(
                integer_part=lst_number_parts[0],
                base=base
            )
            return f"{int_part}"
        else:
            int_part = self._convert_int_part_to_decimal(
                integer_part=lst_number_parts[0],
                base=base
            )
            float_part = self._convert_float_part_to_decimal(
                float_part=lst_number_parts[1],
                base=base
            )
            return f"{int_part}.{float_part}"

    def _convert_int_part_to_decimal(self, integer_part: str, base: int) -> int | str:
        if self._check_for_valid_number(number=integer_part, base=base):
            return int(integer_part, base)
        else:
            return "0"

    def _convert_float_part_to_decimal(self, float_part: str, base: int) -> int | str:
        if self._check_for_valid_number(number=float_part, base=base):
            float_construct: float = 0.0
            digit_rating_float = -1
            for flt in float_part:
                if ord(flt) >= index_char_a_upper:
                    flt = ord(flt) - delta_for_num
                float_construct += int(flt) * (base ** digit_rating_float)
                digit_rating_float -= 1
            return int(str(float_construct)[2:])
        else:
            return "0"

    def _check_for_valid_number(self, number: str, base: int) -> bool:
        for char in number:
            if ord(char) - delta_for_num >= 10:
                char = ord(char) - delta_for_num
            if int(char) >= base:
                ErrorMessage(
                    title=mistake[self.lang],
                    message=error_wrong_base(base)[self.lang],
                    width=error_wrong_base_width,
                    height=error_window_height,
                    button_width=error_window_button_width
                )
                return False
        return True

    def _convert_to_base2(self, decimal_num: int | float, base2: int) -> str:
        if base2 == 10:
            return str(decimal_num)
        if isinstance(decimal_num, int):
            return self._get_int_part(
                decimal_num=decimal_num,
                base2=base2
            )
        else:
            return self._get_int_part(
                decimal_num=int(decimal_num),
                base2=base2
            ) + "." + self._get_float_part(
                float_num=decimal_num - int(decimal_num),
                base2=base2
            )

    def _get_int_part(self, decimal_num: int, base2: int) -> str:
        int_part = ""
        while decimal_num != 0:
            num_buffer = decimal_num % base2
            if num_buffer >= 10:
                num_buffer = self.dic_bigger_than_10[num_buffer]
            int_part = str(num_buffer) + int_part
            decimal_num //= base2
        return int_part

    def _get_float_part(self, float_num: float, base2: int) -> str:
        float_part = ""
        count = 0
        while count <= len(str(float_num)[2:]):
            float_num *= base2
            if int(float_num) >= 10:
                float_part += self.dic_bigger_than_10[int(float_num)]
            else:
                float_part += str(int(float_num))
            count += 1
            float_num -= int(float_num)
        return float_part
