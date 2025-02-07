from dearpygui.dearpygui import (
    window,
    group,
    add_button,
    add_text,
    bind_item_font,
    add_slider_int,
    add_input_text,
    set_value,
    get_value,
    stop_dearpygui
)
from modules.windows_parameters import windows_height, windows_width
from modules.Types import MainMenu, FontRegistry
from modules.ErrorMessage import ErrorMessage
from modules.num_sys_parameters import (
    index_char_a_upper,
    index_char_z_upper,
    delta_for_num,
    bases_default_value,
    bases_min_value,
    bases_max_value,
    menu_buttons_width,
    title_num_sys_pos,
    num_input_text_pos,
    base_from_slider_pos,
    base_to_slider_pos,
    num_to_pos,
    number,
    number_base,
    result_number_base,
    result_number,
    mistake,
    error_empty_num,
    error_empty_num_return,
    error_wrong_base,
    error_empty_num_width,
    error_wrong_base_width,
    error_window_height,
    error_window_button_width, input_text_sliders_width
)
from modules.main_config import TITLES


class NumericalSystem:

    def __init__(self,
                 lang: int,
                 main_menu: MainMenu,
                 font_header: FontRegistry.get_font_header,
                 font_num_sys: FontRegistry.get_font_calculator,
                 ) -> None:
        self.lang = lang
        self.dic_bigger_than_10 = {index - delta_for_num: chr(index) for index in range(
            index_char_a_upper,
            index_char_z_upper + 1
        )}
        with window(
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                tag="numerical_system",
                width=windows_width.get("numerical_system"),
                height=windows_height.get("numerical_system"),
                show=False
        ) as self.numerical_system:
            with group(horizontal=True):
                title_num_sys = add_text(
                    default_value=TITLES["num_sys"][self.lang],
                    pos=title_num_sys_pos[lang]
                )
                bind_item_font(title_num_sys, font_header)
            with group(horizontal=True):
                add_text(number[self.lang])
                self.num = add_input_text(
                    width=input_text_sliders_width,
                    pos=num_input_text_pos
                )
                bind_item_font(self.num, font_num_sys)
            with group(horizontal=True):
                add_text(number_base[self.lang])
                self.base_from = add_slider_int(
                    tag="base_from",
                    default_value=bases_default_value,
                    min_value=bases_min_value,
                    max_value=bases_max_value,
                    width=input_text_sliders_width,
                    pos=base_from_slider_pos
                )
            with group(horizontal=True):
                add_text(result_number_base[self.lang])
                self.base_to = add_slider_int(
                    tag="base_to",
                    default_value=bases_default_value,
                    min_value=bases_min_value,
                    max_value=bases_max_value,
                    width=input_text_sliders_width,
                    pos=base_to_slider_pos
                )
            with group(horizontal=True):
                add_text(result_number[self.lang])
                self.num_to = add_input_text(
                    readonly=True,
                    tag="num_to",
                    width=input_text_sliders_width,
                    pos=num_to_pos
                )
                bind_item_font(self.num_to, font_num_sys)
            add_text("")
            with group(horizontal=True):
                add_button(
                    label=TITLES["convert"][self.lang],
                    callback=self.count,
                    width=menu_buttons_width
                )
                add_button(
                    label=TITLES["main_menu"][self.lang],
                    callback=main_menu.go_to_main_menu,
                    width=menu_buttons_width
                )
                add_button(
                    label=TITLES["exit"][self.lang],
                    callback=self.close,
                    width=menu_buttons_width
                )

    def get_numerical_system(self):
        return self.numerical_system

    @staticmethod
    def close():
        stop_dearpygui()

    def count(self):
        set_value(self.num_to, '')
        if not get_value(self.num):
            ErrorMessage(
                title=mistake[self.lang],
                message=error_empty_num[self.lang],
                width=error_empty_num_width,
                height=error_window_height,
                button_width=error_window_button_width
            )
            return error_empty_num_return[self.lang]
        set_value(
            self.num_to,
            self.convert_x_y(
                n=get_value(self.num),
                base=int(get_value(self.base_from)),
                base2=int(get_value(self.base_to))
            )
        )

    def convert_x_y(self, n: str, base: int, base2: int) -> str | int | float | ErrorMessage:
        n = n.upper()
        for char in n:
            if char == ".":
                continue
            if ord(char) - delta_for_num >= 10:
                char = ord(char) - delta_for_num
            if int(char) >= base:
                ErrorMessage(
                    title=mistake[self.lang],
                    message=error_wrong_base(base)[self.lang],
                    width=error_wrong_base_width[self.lang],
                    height=error_window_height,
                    button_width=error_window_button_width
                )
                return ""
        if base == base2:
            return n
        lst_10 = str(n).split(".")
        if len(lst_10) == 2:
            dict_10 = {
                "integer": lst_10[0],
                "float": lst_10[1]
            }
        else:
            dict_10 = {
                "integer": lst_10[0]
            }
        if base2 == 10:
            return self.convert_to_decimal(dict_10=dict_10, base=base)
        else:
            decimal_num = self.convert_to_decimal(dict_10=dict_10, base=base)
            return self.convert_to_base2(decimal_num=decimal_num, base2=base2)

    @staticmethod
    def convert_to_decimal(dict_10: dict, base: int) -> int | float:
        integer = dict_10["integer"]
        integer_part = int(integer, base)
        float_part = 0
        if len(dict_10) == 2:
            float_ = dict_10["float"]
            digit_rating_float = -1
            for number_ in float_:
                if ord(number_) >= index_char_a_upper:
                    number_ = ord(number_) - delta_for_num
                float_part += int(number_) * (base**digit_rating_float)
                digit_rating_float -= 1
        return float(str(integer_part) + "." + str(float_part)[2:]) if len(dict_10) == 2 else integer_part

    def convert_to_base2(self, decimal_num: int | float, base2: int) -> str:
        if isinstance(decimal_num, int):
            return self.get_int_part(decimal_num=decimal_num, base2=base2)
        else:
            return self.get_int_part(
                decimal_num=int(decimal_num),
                base2=base2
            ) + "." + self.get_float_part(
                float_num=decimal_num - int(decimal_num),
                base2=base2
            )

    def get_int_part(self, decimal_num: int, base2: int) -> str:
        int_part = ""
        while decimal_num != 0:
            num_buffer = decimal_num % base2
            if num_buffer >= 10:
                num_buffer = self.dic_bigger_than_10[num_buffer]
            int_part = str(num_buffer) + int_part
            decimal_num //= base2
        return int_part

    def get_float_part(self, float_num: float, base2: int) -> str:
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
