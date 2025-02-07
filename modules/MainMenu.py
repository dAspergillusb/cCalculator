from dearpygui.dearpygui import (
    window,
    group,
    add_text,
    bind_item_font,
    add_button,
    set_item_pos,
    get_item_width,
    set_viewport_width,
    set_viewport_height,
    set_viewport_min_width,
    set_viewport_min_height,
    set_viewport_max_width,
    set_viewport_max_height,
    set_viewport_pos,
    configure_item,
    set_viewport_title,
    stop_dearpygui,
    handler_registry,
    add_key_press_handler,
    mvKey_Escape
)
from modules.windows_parameters import windows_height, windows_width
from modules.main_menu_parameters import (
    main_menu_buttons,
    main_menu_buttons_tags,
    start_tag_num,
    delta_tag,
    start_pos_y,
    delta_pos_y,
    center_text_title,
    buttons_width
)
from modules.Calculator import Calculator
from modules.GraphicsDerivative import GraphicsDerivative
from modules.Graphics import Graphics
from modules.NumericalSystem import NumericalSystem
from modules.NumericaSystemArithmetic import NumericalSystemArithmetic
from modules.Types import FontRegistry, Themes
from modules.main_config import TITLES


class MainMenu:

    def __init__(self, lang: int, title: str, font: FontRegistry, themes: Themes, resolution: tuple[int, int]) -> None:
        self.horizontal_resolution, self.vertical_resolution = resolution
        set_viewport_max_width(windows_width.get("main_menu"))
        set_viewport_min_width(windows_width.get("main_menu"))
        set_viewport_max_height(windows_height.get("main_menu"))
        set_viewport_min_height(windows_height.get("main_menu"))
        font_header = font.get_font_header()
        font_calculator = font.get_font_calculator()
        self.lang = lang
        functions_dict = {
            "go_to_calculator": self.go_to_calculator,
            "go_to_numerical_system": self.go_to_numerical_system,
            "go_to_numerical_system_arithmetic": self.go_to_numerical_system_arithmetic,
            "go_to_graphics": self.go_to_graphics,
            "go_to_derivative": self.go_to_derivative,
            "close": self.close
        }
        tag_num = start_tag_num
        pos_y = start_pos_y
        with window(
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                tag="main_menu",
                width=windows_width.get("main_menu"),
                height=windows_height.get("main_menu"),
                show=True,
        ) as self.main_menu:
            with group(horizontal=True):
                title_gen = add_text(
                    default_value=title,
                    pos=center_text_title[lang]
                )
                bind_item_font(title_gen, font_header)
            with group():
                for button in main_menu_buttons:
                    add_button(
                        label=main_menu_buttons[button][lang],
                        width=buttons_width,
                        callback=functions_dict[button],
                        tag=main_menu_buttons_tags[tag_num]
                    )
                    set_item_pos(
                        item=main_menu_buttons_tags[tag_num],
                        pos=[
                            windows_width.get("main_menu") // 2 - get_item_width(main_menu_buttons_tags[tag_num]) // 2,
                            pos_y
                        ]
                    )
                    tag_num += delta_tag
                    pos_y += delta_pos_y
        self.calculator = Calculator(
            lang=lang,
            main_menu=self,
            font_header=font_header,
            font_calculator=font_calculator,
            themes=themes
        )
        self.derivative = GraphicsDerivative(
            lang=lang,
            main_menu=self,
            font_header=font_header
        )
        self.graphics = Graphics(
            lang=lang,
            main_menu=self,
            font_header=font_header,
            themes=themes
        )
        self.numerical_system = NumericalSystem(
            lang=lang,
            main_menu=self,
            font_header=font_header,
            font_num_sys=font_calculator
        )
        self.numerical_system_arithmetic = NumericalSystemArithmetic(
            lang=lang,
            main_menu=self,
            font_header=font_header,
            font_num_sys_arith=font_calculator,
            themes=themes
        )
        with handler_registry():
            add_key_press_handler(
                mvKey_Escape,
                callback=self.close
            )

    def get_main_menu(self):
        return self.main_menu

    def go_to_main_menu(self):
        viewport_x_pos = self.horizontal_resolution // 2 - windows_width["main_menu"] // 2
        viewport_y_pos = self.vertical_resolution // 2 - windows_height["main_menu"] // 2
        configure_item(self.numerical_system.get_numerical_system(), show=False)
        configure_item(self.calculator.get_calculator(), show=False)
        configure_item(self.calculator.get_key_handler_calculator(), show=False)
        configure_item(self.graphics.get_graphics(), show=False)
        configure_item(self.derivative.get_derivative(), show=False)
        configure_item(self.numerical_system_arithmetic.get_numerical_system_arithmetic(), show=False)
        set_viewport_pos([viewport_x_pos, viewport_y_pos])
        set_viewport_title(TITLES["main_title"][self.lang])
        set_viewport_width(windows_width.get("main_menu"))
        set_viewport_height(windows_height.get("main_menu"))
        set_viewport_max_width(windows_width.get("main_menu"))
        set_viewport_min_width(windows_width.get("main_menu"))
        set_viewport_max_height(windows_height.get("main_menu"))
        set_viewport_min_height(windows_height.get("main_menu"))
        configure_item(self.main_menu, show=True)

    def go_to_calculator(self):
        viewport_x_pos = self.horizontal_resolution // 2 - windows_width["calculator"] // 2
        viewport_y_pos = self.vertical_resolution // 2 - windows_height["calculator"] // 2
        configure_item(self.main_menu, show=False)
        set_viewport_pos([viewport_x_pos, viewport_y_pos])
        set_viewport_title(TITLES["calc"][self.lang])
        set_viewport_width(windows_width.get("calculator"))
        set_viewport_height(windows_height.get("calculator"))
        set_viewport_max_width(windows_width.get("calculator"))
        set_viewport_min_width(windows_width.get("calculator"))
        set_viewport_max_height(windows_height.get("calculator"))
        set_viewport_min_height(windows_height.get("calculator"))
        configure_item(self.calculator.get_calculator(), show=True)
        configure_item(self.calculator.get_key_handler_calculator(), show=True)

    def go_to_numerical_system(self):
        viewport_x_pos = self.horizontal_resolution // 2 - windows_width["numerical_system"] // 2
        viewport_y_pos = self.vertical_resolution // 2 - windows_height["numerical_system"] // 2
        configure_item(self.main_menu, show=False)
        set_viewport_pos([viewport_x_pos, viewport_y_pos])
        set_viewport_title(TITLES["num_sys"][self.lang])
        set_viewport_width(windows_width.get("numerical_system"))
        set_viewport_height(windows_height.get("numerical_system"))
        set_viewport_max_width(windows_width.get("numerical_system"))
        set_viewport_min_width(windows_width.get("numerical_system"))
        set_viewport_max_height(windows_height.get("numerical_system"))
        set_viewport_min_height(windows_height.get("numerical_system"))
        configure_item(self.numerical_system.get_numerical_system(), show=True)

    def go_to_numerical_system_arithmetic(self):
        viewport_x_pos = self.horizontal_resolution // 2 - windows_width["numerical_system_arithmetic"] // 2
        viewport_y_pos = self.vertical_resolution // 2 - windows_height["numerical_system_arithmetic"] // 2
        configure_item(self.main_menu, show=False)
        set_viewport_pos([viewport_x_pos, viewport_y_pos])
        set_viewport_title(TITLES["num_sys_arith"][self.lang])
        set_viewport_width(windows_width.get("numerical_system_arithmetic"))
        set_viewport_height(windows_height.get("numerical_system_arithmetic"))
        set_viewport_max_width(windows_width.get("numerical_system_arithmetic"))
        set_viewport_min_width(windows_width.get("numerical_system_arithmetic"))
        set_viewport_max_height(windows_height.get("numerical_system_arithmetic"))
        set_viewport_min_height(windows_height.get("numerical_system_arithmetic"))
        configure_item(self.numerical_system_arithmetic.get_numerical_system_arithmetic(), show=True)

    def go_to_graphics(self):
        viewport_x_pos = self.horizontal_resolution // 2 - windows_width["graphics"] // 2
        viewport_y_pos = self.vertical_resolution // 2 - windows_height["graphics"] // 2
        configure_item(self.main_menu, show=False)
        set_viewport_pos([viewport_x_pos, viewport_y_pos])
        set_viewport_title(TITLES["graphs"][self.lang])
        set_viewport_width(windows_width.get("graphics"))
        set_viewport_height(windows_height.get("graphics"))
        set_viewport_max_width(windows_width.get("graphics"))
        set_viewport_min_width(windows_width.get("graphics"))
        set_viewport_max_height(windows_height.get("graphics"))
        set_viewport_min_height(windows_height.get("graphics"))
        configure_item(self.graphics.get_graphics(), show=True)

    def go_to_derivative(self):
        viewport_x_pos = self.horizontal_resolution // 2 - windows_width["derivative"] // 2
        viewport_y_pos = self.vertical_resolution // 2 - windows_height["derivative"] // 2
        configure_item(self.main_menu, show=False)
        set_viewport_pos([viewport_x_pos, viewport_y_pos])
        set_viewport_title(TITLES["deriv"][self.lang])
        set_viewport_width(windows_width.get("derivative"))
        set_viewport_height(windows_height.get("derivative"))
        set_viewport_max_width(windows_width.get("derivative"))
        set_viewport_min_width(windows_width.get("derivative"))
        set_viewport_max_height(windows_height.get("derivative"))
        set_viewport_min_height(windows_height.get("derivative"))
        configure_item(self.derivative.get_derivative(), show=True)

    @staticmethod
    def close():
        stop_dearpygui()



