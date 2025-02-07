from math import pi
from dearpygui.dearpygui import (
    window,
    group,
    add_text,
    add_button,
    add_input_text,
    bind_item_font,
    handler_registry,
    add_key_press_handler,
    add_combo,
    get_value,
    set_value,
    stop_dearpygui,
    delete_item,
    get_item_width,
    add_checkbox,
    configure_item,
    bind_item_theme,
    get_item_pos,
)
from modules.ErrorMessage import ErrorMessage
from modules.calculator_parameters import (
    title_pos,
    error_zero_div_width,
    error_factorial_width,
    error_height,
    error_button_width,
    error_factorial,
    error_zero_division,
    mistake,
    button_height,
    button_width,
    input_text_width,
    button_main_menu_exit_width,
    first_block_buttons,
    second_block_buttons,
    third_block_buttons,
    key_handler,
    trigonometry_values_list,
    rounded_for,
    round_for_digits_list,
    shift_block_buttons,
    root_titles,
    input_number_root_width,
    spacing_with_value_types_options,
    is_rational_fractions,
    radians_degrees_combo_width,
    rounded_combo_width,
    delta_for_root_button,
    radical_x_window_width,
    radical_x_window_height,
    horizontal_spacing_for_buttons_blocks,
    old_operations_input_text_height,
    additional_button_width
)
from modules.font_chars import (
    CHARS_INT,
    CHARS_DICT_SUPERSCRIPT,
    ROOT_CHAR
)
from modules.calculation_functions import calculate
from modules.windows_parameters import windows_height, windows_width
from modules.Types import MainMenu, FontRegistry, Themes
from modules.main_config import TITLES


class Calculator:

    def __init__(self,
                 lang: int,
                 main_menu: MainMenu,
                 font_header: FontRegistry.get_font_header,
                 font_calculator: FontRegistry.get_font_calculator,
                 themes: Themes
                 ) -> None:
        self.theme_activated_: int = themes.get_shifted_theme()
        self.theme_deactivated_: int = themes.get_global_theme()
        self.lang: int = lang
        self.round_to: int = 14
        self.trigonometry_value: float = pi / 180
        self.result_ok: bool = False
        self.add_func: bool = False
        self.power_xy_activated: bool = False
        self.first_block_buttons_rev_keys_values: dict = {value: key for key, value in first_block_buttons.items()}
        self.chars_dict_rev_keys_values: dict = {value: key for key, value in CHARS_DICT_SUPERSCRIPT.items()}
        with window(
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                tag="calculator",
                width=windows_width.get("calculator"),
                height=windows_height.get("calculator"),
                show=False
        ) as self.calculator:
            with group():
                title_calc = add_text(
                    default_value=TITLES["calc"][self.lang],
                    pos=title_pos[self.lang]
                )
                bind_item_font(title_calc, font_header)
            self.text = add_input_text(readonly=True, width=input_text_width)
            bind_item_font(self.text, font_calculator)
            self.text_old_operations = add_input_text(
                readonly=True,
                width=input_text_width,
                height=old_operations_input_text_height,
                multiline=True
            )
            bind_item_font(self.text_old_operations, font_calculator)

            with group(horizontal=True, horizontal_spacing=spacing_with_value_types_options[self.lang]):
                self.rational = add_checkbox(
                    label=is_rational_fractions[self.lang],
                    default_value=False
                )
                self.radians_degrees = add_combo(
                    trigonometry_values_list[self.lang],
                    default_value=trigonometry_values_list[self.lang][1],
                    width=radians_degrees_combo_width,
                    callback=self._trigonometry_values)
                with group(horizontal=True):
                    add_text(default_value=rounded_for[self.lang])
                    self.rounded = add_combo(
                        round_for_digits_list,
                        default_value=round_for_digits_list[-1],
                        width=rounded_combo_width,
                        callback=None
                    )
            with group(horizontal=True, horizontal_spacing=horizontal_spacing_for_buttons_blocks):
                with group():
                    index = 0
                    buttons = tuple(first_block_buttons.items())
                    while index < len(buttons):
                        with group(horizontal=True):
                            for tag, label in buttons[index:index + 3]:
                                add_button(
                                    label=label,
                                    tag=tag,
                                    width=button_width,
                                    height=button_height,
                                    callback=self._check_for_char
                                )
                        index += 3
                with group():
                    buttons = tuple(second_block_buttons.items())
                    for tag, label in buttons:
                        add_button(
                            label=label,
                            tag=tag,
                            width=button_width,
                            height=button_height,
                            callback=self._check_for_char
                        )
                with handler_registry(show=False) as self.key_handler_calculator:
                    for key, value in tuple(key_handler.items()):
                        add_key_press_handler(
                            key=value,
                            tag=key,
                            callback=self._check_for_char,
                        )
                    """add_key_press_handler(
                        mvKey_Escape,
                        callback=self.close
                    )"""
                with group():
                    add_button(
                        label=third_block_buttons["additional_functions"][self.lang],
                        tag=tuple(third_block_buttons.keys())[0],
                        width=additional_button_width,
                        height=button_height,
                        callback=self._additional_functions
                    )
                    index = 1
                    buttons = tuple(third_block_buttons.items())
                    while index < len(buttons):
                        with group(horizontal=True):
                            for tag, label in buttons[index:index + 3]:
                                add_button(
                                    label=label,
                                    tag=tag,
                                    width=button_width,
                                    height=button_height,
                                    callback=self._check_for_function
                                )
                        index += 3
                    index = 0
                    buttons = tuple(shift_block_buttons.items())
                    while index < len(buttons):
                        with group(horizontal=True):
                            for tag, label in buttons[index:index + 3]:
                                add_button(
                                    label=label,
                                    tag=tag,
                                    width=button_width,
                                    height=button_height,
                                    callback=self._check_for_function,
                                    show=False,
                                    pos=[0, 0]
                                )
                        index += 3
            with group(horizontal=True):
                add_button(
                    label=TITLES["main_menu"][lang],
                    callback=main_menu.go_to_main_menu,
                    width=button_main_menu_exit_width
                )
                add_button(
                    label=TITLES["exit"][lang],
                    callback=self.close,
                    width=button_main_menu_exit_width
                )

    def get_calculator(self) -> int | str:
        return self.calculator

    def get_key_handler_calculator(self) -> int | str:
        return self.key_handler_calculator

    @staticmethod
    def close() -> None:
        stop_dearpygui()

    def result(self) -> None:
        self.result_ok = not self.result_ok
        num: str = get_value(self.text)
        if "ln" in num:
            set_value(self.text, num.replace("ln", "log"))
        if "%" in num:
            percent: list[int] = list(map(int, num.split("%")))
            set_value(self.text, f"{percent[1]} * {percent[0]} / 100")
        try:
            expression_result = calculate(
                expression=get_value(self.text),
                rational_fraction=get_value(self.rational),
                trigonometry_value=self.trigonometry_value
            )
        except (ValueError, SyntaxError):
            return self._insert_result(num, "Some problems in expression")
        return self._insert_result(num, expression_result)

    def _additional_functions(self):
        if self.add_func:
            self._deactivate_additional_functions()
        else:
            self._activate_additional_functions()
        self.add_func = not self.add_func

    def _activate_additional_functions(self):
        bind_item_theme("additional_functions", self.theme_activated_)
        deactivate_function_tags = tuple(third_block_buttons.keys())[1:]
        activate_function_tags = tuple(shift_block_buttons.keys())
        buttons_position = [get_item_pos(tag) for tag in deactivate_function_tags]
        position_index = 0
        for deactivate_tag, activate_tag in zip(deactivate_function_tags, activate_function_tags):
            configure_item(
                deactivate_tag,
                show=False,
                pos=[0, 0]

            )
            configure_item(
                activate_tag,
                show=True,
                pos=buttons_position[position_index]
            )
            position_index += 1

    def _deactivate_additional_functions(self):
        bind_item_theme("additional_functions", self.theme_deactivated_)
        deactivate_function_tags = tuple(shift_block_buttons.keys())
        activate_function_tags = tuple(third_block_buttons.keys())[1:]
        buttons_position = [get_item_pos(tag) for tag in deactivate_function_tags]
        position_index = 0
        for deactivate_tag, activate_tag in zip(deactivate_function_tags, activate_function_tags):
            configure_item(
                deactivate_tag,
                show=False,
                pos=[0, 0]

            )
            configure_item(
                activate_tag,
                show=True,
                pos=buttons_position[position_index]
            )
            position_index += 1

    def _insert_result(self, num: str, expression_result: int | float | str) -> None:
        if isinstance(expression_result, float) and not get_value(self.rational):
            rounded = get_value(self.rounded)
            round_to = None if rounded == "0" else int(rounded)
            expression_result = round(expression_result, round_to)

        self.add_to_history(
            eq=num,
            result=expression_result
        )
        return set_value(self.text, expression_result)

    def add_to_history(self, eq: str, result: float | str) -> None:
        return set_value(
            item=self.text_old_operations,
            value=f"{eq}\t\t=\t\t{result}\n{get_value(self.text_old_operations)}"
            )

    def erase(self) -> None:
        return set_value(self.text, '')

    def delete(self) -> None:
        expression = get_value(self.text)
        if expression[-1] == " ":
            return set_value(self.text, expression[:-3])
        else:
            return set_value(self.text, get_value(self.text)[:-1])

    def radical_x(self) -> None:
        with window(
                modal=True,
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                width=radical_x_window_width,
                height=radical_x_window_height
        ) as root_window:
            with group(horizontal=True):
                with group():
                    add_text(default_value=root_titles[0][self.lang])
                    add_text(default_value=root_titles[1][self.lang])
                with group():
                    input_number = add_input_text(default_value="81", width=input_number_root_width[self.lang])
                    input_root = add_input_text(default_value="4", width=input_number_root_width[self.lang])
            with group(horizontal=True, horizontal_spacing=2):
                add_button(
                    label="Ok",
                    width=get_item_width(root_window) // 2 - delta_for_root_button,
                    callback=lambda: self._insert_radical_x(
                        get_value(input_number),
                        get_value(input_root),
                        root_window=root_window)
                )
                add_button(
                    label=root_titles[2][self.lang],
                    width=get_item_width(root_window) // 2 - delta_for_root_button,
                    callback=lambda: delete_item(root_window)
                )

    def _insert_radical_x(self, insert_number: str, insert_root: str, *, root_window: window) -> None:
        buffer = get_value(self.text)
        if buffer and buffer[-1].isdecimal():
            return None
        set_value(self.text, buffer + f"{self.chars_dict_rev_keys_values[insert_root]}{chr(ROOT_CHAR)}{insert_number}")
        delete_item(root_window)

    def percentage(self) -> None:
        if get_value(self.text) == '':
            return set_value(self.text, '')
        string_lst: list[str] = get_value(self.text).split(' ')
        if len(string_lst) >= 3:
            num_float = float(string_lst[-3]) * float(string_lst[-1]) / 100
            num = get_value(self.text)[:-len(string_lst[-1])] + str(num_float)
            set_value(self.text, num)
        elif not string_lst[-1].isdecimal():
            return None
        else:
            num = string_lst[0]
            num += "%" if num.isdecimal() else ""
            set_value(self.text, num)

    def _trigonometry_values(self) -> None:
        trigonometry_value = get_value(self.radians_degrees)
        match trigonometry_value:
            case "Радианы" | "Radians":
                self.trigonometry_value = 1
            case "Градусы" | "Degrees":
                self.trigonometry_value = pi / 180
            case "Грады" | "Grads":
                self.trigonometry_value = pi / 200

    def _check_for_char(self, tag: str | int) -> None | ErrorMessage:
        tag = tag[:tag.index("_")] if "_" in tag else tag
        match tag:
            case "erase":
                return self.erase()
            case "delete":
                return self.delete()
            case "parenthesis":
                return self.parenthesis()
            case "dot":
                return self.dot()
            case "plus-minus":
                return self.plus_minus()
            case "plus" | "minus" | "multiply" | "divide":
                return self._insert_action(tag=tag)
            case "result":
                return self.result()
            case _:
                if self.power_xy_activated:
                    char = self.chars_dict_rev_keys_values[first_block_buttons[tag]]
                else:
                    char = first_block_buttons[tag]
                return self._insert_number(char)

    def _insert_action(self, tag: str) -> None:
        self._is_result_ok(reset_input_text=False)
        char = second_block_buttons[tag]
        num = get_value(self.text)
        if num == '':
            return set_value(self.text, '')
        if num[-1] == ' ':
            return None
        num += f' {char} '
        set_value(self.text, num)

    def _insert_number(self, char: str) -> None:
        self._is_result_ok()
        num = get_value(self.text)
        num += char
        return set_value(self.text, num)

    def _check_for_function(self, tag: str) -> None:
        self._is_result_ok()
        num: str = get_value(self.text)
        if tag == "square" or tag == "powerXY":
            return self._insert_function(tag=tag)
        if tag == "radX":
            return self.radical_x()
        #if num and tag not in ["percentage", "reverse_num", "factorial"]:
        #    return None
        if tag == "percentage":
            return self.percentage()
        return self._insert_function(tag=tag)

    def _insert_function(self, tag: str) -> None:
        buffer: str = get_value(self.text)
        match tag:
            case "reverse_num":
                return set_value(self.text, f"1 / ({buffer})")
            case "square":
                return set_value(self.text, buffer + chr(CHARS_INT[2]))
            case "powerXY":
                return self._activate_deactivate_power_xy_insert(tag="powerXY")
            case "rad2" | "rad3":
                return set_value(
                    self.text,
                    f"{buffer}{self.chars_dict_rev_keys_values[tag[-1]]}{chr(ROOT_CHAR)}")
            case "factorial":
                if buffer and buffer[-1].isdecimal():
                    return set_value(self.text, buffer + "!")
                else:
                    return None
        return set_value(self.text, buffer + f"{tag}(")

    def _activate_deactivate_power_xy_insert(self, tag: str) -> None:
        if self.power_xy_activated:
            bind_item_theme(tag, theme=self.theme_deactivated_)
            self._deactivate_power_xy_insert()
        else:
            bind_item_theme(tag, theme=self.theme_activated_)
            self._activate_power_xy_insert()
        self.power_xy_activated = not self.power_xy_activated

    def _activate_power_xy_insert(self):
        for button_label in CHARS_DICT_SUPERSCRIPT.values():
            configure_item(
                self.first_block_buttons_rev_keys_values[button_label],
                label=self.chars_dict_rev_keys_values[button_label],
            )

    def _deactivate_power_xy_insert(self):
        for button_label in self.chars_dict_rev_keys_values.values():
            configure_item(
                self.first_block_buttons_rev_keys_values[CHARS_DICT_SUPERSCRIPT[button_label]],
                label=CHARS_DICT_SUPERSCRIPT[button_label]
            )

    def _is_result_ok(self, reset_input_text: bool = True) -> None:
        if reset_input_text:
            if self.result_ok:
                set_value(self.text, "")
                self.result_ok = not self.result_ok
        else:
            if self.result_ok:
                self.result_ok = not self.result_ok

    def dot(self) -> None:
        num = get_value(self.text)
        if num[-1] == '.':
            return None
        num += '.'
        set_value(self.text, num)

    def plus_minus(self) -> None:
        num: str = get_value(self.text)
        list_from_num: list[str] = num.split()
        if num == '':
            return set_value(self.text, '')
        if num.isdecimal():
            return set_value(self.text, '-' + num)
        elif num[0] == '-':
            return set_value(self.text, num[1:])
        elif list_from_num[-1].isdecimal():
            last_num = "(-" + list_from_num[-1] + ")"
            num = num[:-len(last_num[2:-1])] + last_num
            return set_value(self.text, num)
        elif "(-" in list_from_num[-1]:
            return set_value(
                self.text,
                get_value(self.text).replace("(", "").replace("-", "").replace(")", ""))
        elif num[0] == "(" and num[-1] == ")":
            return set_value(self.text, "-" + num)
        elif ("." in num and
              (
                      num.split(".")[0].isdecimal() or
                      num.split(".")[1].isdecimal()
                )
            ):
            return set_value(self.text, "-" + num)
        else:
            return None

    def parenthesis(self) -> None:
        expression: str = get_value(self.text)
        if not expression:
            return set_value(self.text, "(")
        elif expression[-1] == "(":
            return set_value(self.text, f"{expression}(")
        elif expression[-1] == " ":
            return set_value(self.text, f"{expression}(")
        elif expression[-1].isdecimal() and "(" in expression:
            return set_value(self.text, f"{expression})")
        elif expression.isdecimal():
            return set_value(self.text, f"({expression}")
        elif (
            expression[-1] == ")" and
            expression.count("(") - expression.count(")") >= 1
            ):
            count_close = expression.count("(") - expression.count(")")
            return set_value(self.text, expression + ")" * count_close)
        elif (
                expression[-1] in CHARS_DICT_SUPERSCRIPT.keys() or
                expression[-1] == "!"
                ):
            return set_value(self.text, f"{expression})")

        '''    
        num: str = get_value(self.text)
        if num.isdecimal():
            num = "(" + num
        elif num == "":
            num += "("
        elif num.find("(") == -1 and num[-1] == " ":
            num += "("
        elif (num.find(")") == -1 and
              num.count("(") == 1 and
              num[-1] != "(" and
              num[-1].isdecimal()):
            num += ")"
        elif num.count('(') == num.count(")") and num[-1] != ")" and not num[-1].isdecimal():
            num += "("
        elif num.count("(") == num.count(")") + 1 and num[-1].isdecimal():
            num += ")"
        elif "(" in num.split()[-2]:
            num += "("
        elif "(" in num.split()[-3] and num[-1].isdecimal():
            count = 0
            for item in num.split():
                if "(" in item:
                    count += 1
                elif ")" in item:
                    count -= 1
            num += ")" * count
        else:
            num += ")"
        set_value(self.text, num)
        '''
