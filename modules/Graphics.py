from dearpygui.dearpygui import (
    window,
    group,
    add_button,
    add_text,
    bind_item_font,
    add_input_text,
    add_radio_button,
    plot,
    add_plot_legend,
    add_plot_axis,
    mvXAxis,
    mvYAxis,
    add_line_series,
    stop_dearpygui,
    set_value,
    get_value,
    set_axis_limits,
    set_item_label,
    set_axis_limits_auto,
    reset_axis_ticks,
    configure_item,
    bind_item_theme
)
from sympy.core.numbers import Float, Zero, Integer
from modules.windows_parameters import windows_height, windows_width
from modules.Types import MainMenu, FontRegistry, Themes
from modules.main_config import TITLES
from modules.calculation_functions import calculate_graphs
from modules.graphics_parameters import (
    plot_width,
    plot_height,
    input_text_x_y_width,
    min_x_y_val,
    max_x_y_val,
    func_1_width,
    func_2_width,
    func_3_width,
    build_graph_width,
    build_graph_height,
    build_graph_pos,
    main_menu_width,
    main_menu_height,
    main_menu_pos,
    exit_width,
    title_graph_pos,
    plot_x_axis,
    plot_y_axis,
    min_val_x,
    min_val_y,
    max_val_x,
    max_val_y,
    axis_alignment,
    graphs_quantity,
    choose_x_y_radio_text,
    choose_quantity_radio_text,
    text_func_f,
    text_func_g,
    text_func_h,
    build_graph
)


class Graphics:

    def __init__(self, lang: int, main_menu: MainMenu, font_header: FontRegistry.get_font_header, themes: Themes):
        self.lang = lang
        self.disabled_theme = themes.get_disabled_theme()
        self.global_theme = themes.get_global_theme()
        zeros_value = range(100)
        self.func_data_x = [0 for _ in zeros_value]
        self.func_data_y_1 = [0 for _ in zeros_value]
        self.func_data_y_2 = [0 for _ in zeros_value]
        self.func_data_y_3 = [0 for _ in zeros_value]
        with window(
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                tag="graphics",
                width=windows_width.get("graphics"),
                height=windows_height.get("graphics"),
                show=False
        ) as self.graphics:
            with group():
                title_graph = add_text(
                    default_value=TITLES["graphs"][self.lang],
                    pos=title_graph_pos[self.lang]
                )
                bind_item_font(title_graph, font_header)

            with plot(width=plot_width, height=plot_height):
                add_plot_legend()
                add_plot_axis(mvXAxis, label=plot_x_axis[self.lang], tag="x_axis")
                add_plot_axis(mvYAxis, label=plot_y_axis[self.lang], tag="y_axis_1")
                add_line_series(
                    self.func_data_x,
                    self.func_data_y_1,
                    label="sin(x)",
                    parent="y_axis_1",
                    tag="graphic_of_func_1"
                )
                add_plot_axis(mvYAxis, label=plot_y_axis[self.lang], tag="y_axis_2")
                add_line_series(
                    self.func_data_x,
                    self.func_data_y_2,
                    label="cos(x)",
                    parent="y_axis_2",
                    tag="graphic_of_func_2"
                )
                add_plot_axis(mvYAxis, label=plot_y_axis[self.lang], tag="y_axis_3")
                add_line_series(
                    self.func_data_x,
                    self.func_data_y_3,
                    label="sin(x) * cos(x)",
                    parent="y_axis_3",
                    tag="graphic_of_func_3"
                )
                tag_graphic_of_func_what = ("graphic_of_func_1", "graphic_of_func_2", "graphic_of_func_3")
                y_axis = ("y_axis_1", "y_axis_2", "y_axis_3")
            with group(horizontal=True):
                add_text(min_val_x[self.lang])
                self.min_x = add_input_text(
                    width=input_text_x_y_width,
                    tag="self.min_x",
                    default_value=min_x_y_val
                )
                add_text(min_val_y[self.lang])
                self.min_y = add_input_text(
                    width=input_text_x_y_width,
                    tag="self.min_y",
                    default_value=min_x_y_val)
                add_text(axis_alignment[self.lang])
                add_text(graphs_quantity[self.lang])
            with group(horizontal=True):
                add_text(max_val_x[self.lang])
                self.max_x = add_input_text(
                    width=input_text_x_y_width,
                    tag="self.max_x",
                    default_value=max_x_y_val)
                add_text(max_val_y[self.lang])
                self.max_y = add_input_text(
                    width=input_text_x_y_width,
                    tag="self.max_y",
                    default_value=max_x_y_val)
                with group(horizontal=True, horizontal_spacing=30):
                    self.choose_x_y = add_radio_button(
                        items=choose_x_y_radio_text[self.lang],
                        default_value=choose_x_y_radio_text[self.lang][0],
                        callback=lambda: self.graphic_calculate("x_axis", y_axis, tag_graphic_of_func_what),
                        horizontal=True
                    )
                    self.choose_quantity_func = add_radio_button(
                        items=choose_quantity_radio_text[self.lang],
                        default_value=choose_quantity_radio_text[self.lang][2],
                        callback=self.num_of_func,
                        horizontal=True
                    )
            with group(horizontal=False):
                with group(horizontal=True):
                    add_text(text_func_f[self.lang])
                    self.func_1 = add_input_text(width=func_1_width, default_value="sin(x)")
                with group(horizontal=True):
                    add_text(text_func_g[self.lang])
                    self.func_2 = add_input_text(width=func_2_width, default_value="cos(x)")
                with group(horizontal=True):
                    add_text(text_func_h[self.lang])
                    self.func_3 = add_input_text(width=func_3_width, default_value="sin(x) * cos(x)")
                add_button(
                    label=build_graph[self.lang],
                    callback=lambda: self.graphic_calculate("x_axis", y_axis, tag_graphic_of_func_what),
                    width=build_graph_width,
                    height=build_graph_height,
                    pos=build_graph_pos
                )
                add_button(
                    label=TITLES["main_menu"][self.lang],
                    callback=main_menu.go_to_main_menu,
                    width=main_menu_width,
                    height=main_menu_height,
                    pos=main_menu_pos
                )
            with group(horizontal=True, pos=[516, 750]):
                # add_button(label="Главное меню", callback=main_menu.go_to_main_menu, width=247)
                add_button(
                    label=TITLES["exit"][self.lang],
                    callback=self.close,
                    width=exit_width
                )

    def get_graphics(self):
        return self.graphics

    @staticmethod
    def close():
        stop_dearpygui()

    def graphic_calculate(
            self,
            x_axis: str,
            y_axis: tuple[str, str, str],
            tag_graphic_of_func_what: tuple[str, str, str]
    ) -> None:
        reset_axis_ticks(x_axis)
        reset_axis_ticks(y_axis[0])
        reset_axis_ticks(y_axis[1])
        reset_axis_ticks(y_axis[2])
        func_data_x_1, func_data_x_2, func_data_x_3 = [], [], []
        func_data_y_1, func_data_y_2, func_data_y_3 = [], [], []
        func: tuple[str, str, str] = (get_value(self.func_1), get_value(self.func_2), get_value(self.func_3))
        func_data_y = (func_data_y_1, func_data_y_2, func_data_y_3)
        func_data_x = (func_data_x_1, func_data_x_2, func_data_x_3)
        delta_x: tuple[float | int, float | int, float | int] = (
            0.1 if "!" not in func[0] else 1,
            0.1 if "!" not in func[1] else 1,
            0.1 if "!" not in func[2] else 1
        )
        x = int(get_value(self.min_x))
        number_func = 1
        while number_func <= self.num_of_func():
            function: str = func[number_func - 1]
            while x <= int(get_value(self.max_x)):
                data_y = calculate_graphs(
                        equation=function,
                        x=x
                    )
                if isinstance(data_y, Float | Zero | Integer | int):
                    func_data_x[number_func - 1].append(x)
                    func_data_y[number_func - 1].append(data_y)
                x += delta_x[number_func - 1]
            x = int(get_value(self.min_x))
            set_value(
                tag_graphic_of_func_what[number_func - 1],
                [func_data_x[number_func - 1],
                 func_data_y[number_func - 1]]
            )
            set_item_label(tag_graphic_of_func_what[number_func - 1], func[number_func - 1])
            number_func += 1
        if get_value(self.choose_x_y) == choose_x_y_radio_text[self.lang][0]:
            set_axis_limits(x_axis, min(func_data_x[0]), max(func_data_x[0]))
            set_axis_limits(y_axis[0], min(func_data_y[0]), max(func_data_y[0]))
            set_axis_limits(
                y_axis[1],
                min([0] if not len(func_data_y[1]) else func_data_y[1]),
                max([0] if not len(func_data_y[1]) else func_data_y[1])
            )
            set_axis_limits(
                y_axis[2],
                min([0] if not len(func_data_y[2]) else func_data_y[2]),
                max([0] if not len(func_data_y[2]) else func_data_y[2])
            )
        if get_value(self.choose_x_y) == choose_x_y_radio_text[self.lang][1]:
            set_axis_limits(x_axis, int(get_value(self.min_x)), int(get_value(self.max_x)))
            set_axis_limits(y_axis[0], int(get_value(self.min_y)), int(get_value(self.max_y)))
            set_axis_limits(y_axis[1], int(get_value(self.min_y)), int(get_value(self.max_y)))
            set_axis_limits(y_axis[2], int(get_value(self.min_y)), int(get_value(self.max_y)))
        if get_value(self.choose_x_y) == choose_x_y_radio_text[self.lang][2]:
            set_axis_limits_auto(x_axis)
            set_axis_limits_auto(y_axis[0])
            set_axis_limits_auto(y_axis[1])
            set_axis_limits_auto(y_axis[2])

    def num_of_func(self) -> int:
        if get_value(self.choose_quantity_func) == choose_quantity_radio_text[self.lang][0]:
            num: int = 1
            configure_item("graphic_of_func_2", show=False)
            configure_item("y_axis_2", show=False)
            configure_item("graphic_of_func_3", show=False)
            configure_item("y_axis_3", show=False)
            bind_item_theme(self.func_2, self.disabled_theme)
            configure_item(self.func_2, readonly=True)
            bind_item_theme(self.func_3, self.disabled_theme)
            configure_item(self.func_3, readonly=True)
        elif get_value(self.choose_quantity_func) == choose_quantity_radio_text[self.lang][1]:
            num: int = 2
            configure_item("graphic_of_func_2", show=True)
            configure_item("y_axis_2", show=True)
            configure_item("graphic_of_func_3", show=False)
            configure_item("y_axis_3", show=False)
            bind_item_theme(self.func_2, self.global_theme)
            configure_item(self.func_2, readonly=False)
            bind_item_theme(self.func_3, self.disabled_theme)
            configure_item(self.func_3, readonly=True)
        else:
            num: int = 3
            configure_item("graphic_of_func_2", show=True)
            configure_item("y_axis_2", show=True)
            configure_item("graphic_of_func_3", show=True)
            configure_item("y_axis_3", show=True)
            bind_item_theme(self.func_2, self.global_theme)
            configure_item(self.func_2, readonly=False)
            bind_item_theme(self.func_3, self.global_theme)
            configure_item(self.func_3, readonly=False)
        return num


