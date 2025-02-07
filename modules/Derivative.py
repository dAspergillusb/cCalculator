from dearpygui.dearpygui import (
    window,
    group,
    bind_item_font,
    add_text,
    add_input_text,
    add_radio_button,
    add_button,
    plot,
    add_plot_legend,
    add_plot_axis,
    add_line_series,
    mvYAxis,
    mvXAxis,
    get_value,
    set_value,
    set_item_label,
    set_axis_limits,
    set_axis_limits_auto,
    texture_registry,
    add_static_texture,
    drawlist,
    stop_dearpygui,
    load_image,
    draw_image,
    delete_item,
)
from asyncio import gather, run
from sympy import diff
from sympy.core.numbers import Float, Zero
from modules.Types import MainMenu, FontRegistry
from modules.windows_parameters import windows_height, windows_width
from modules.main_config import TITLES
from modules.graphics_parameters import (
    input_text_x_y_width,
    min_x_y_val,
    max_x_y_val,
    plot_x_axis,
    plot_y_axis,
    min_val_x,
    min_val_y,
    max_val_x,
    max_val_y,
    axis_alignment,
    choose_x_y_radio_text
)
from modules.derivative_parameters import (
    plot_width,
    plot_height,
    func_y_input_text_width,
    build_der_width,
    build_der_height,
    main_buttons_width,
    title_deriv_pos,
    func_y,
    func_y_der,
    build_der
)
from modules.GetLatexEquationImage import GetLatexEquationImage
from modules.calculation_functions import calculate_graphs


class Derivative:

    def __init__(self, lang: int, main_menu: MainMenu, font_header: FontRegistry.get_font_header):
        self.lang = lang
        zeros_value = range(100)
        self.func_data_x = [0 for _ in zeros_value]
        self.func_data_y = [0 for _ in zeros_value]
        self.draw_list_width, self.draw_list_height = (760, 100)
        with window(
                no_move=True,
                no_collapse=True,
                no_resize=True,
                no_close=True,
                no_title_bar=True,
                tag="derivative",
                width=windows_width.get("derivative"),
                height=windows_height.get("derivative"),
                show=False
        ) as self.derivative:
            with group():
                title_deriv = add_text(
                    default_value=TITLES["deriv"][self.lang],
                    pos=title_deriv_pos[self.lang]
                )
                bind_item_font(title_deriv, font_header)

            with plot(width=plot_width, height=plot_height):
                add_plot_legend()
                add_plot_axis(
                    mvXAxis,
                    label=plot_x_axis[self.lang],
                    tag="x_axis_der"
                )
                add_plot_axis(
                    mvYAxis,
                    label=plot_y_axis[self.lang],
                    tag="y_axis_der"
                )
                add_line_series(
                    self.func_data_x,
                    self.func_data_y,
                    label="sin(x)",
                    parent="y_axis_der",
                    tag="graphic_of_func_der"
                )
            with group(horizontal=True):
                add_text(min_val_x[self.lang])
                self.min_x_der = add_input_text(
                    width=input_text_x_y_width,
                    tag="min_x_der",
                    default_value=min_x_y_val
                )
                add_text(min_val_y[self.lang])
                self.min_y_der = add_input_text(
                    width=input_text_x_y_width,
                    tag="min_y_der",
                    default_value=min_x_y_val
                )
                add_text(axis_alignment[self.lang])
            with group(horizontal=True):
                add_text(max_val_x[self.lang])
                self.max_x_der = add_input_text(
                    width=input_text_x_y_width,
                    tag="max_x_der",
                    default_value=max_x_y_val
                )
                add_text(max_val_y[self.lang])
                self.max_y_der = add_input_text(
                    width=input_text_x_y_width,
                    tag="max_y_der",
                    default_value=max_x_y_val
                )
                self.choose_x_y_der = add_radio_button(
                    items=choose_x_y_radio_text[self.lang],
                    default_value=choose_x_y_radio_text[self.lang][0],
                    callback=lambda: self.graphic_calculate_derivative(func_derivative=get_value(self.func_der)),
                    horizontal=True
                )
            with group(horizontal=True):
                add_text(func_y[self.lang])
                self.func_to_der = add_input_text(
                    width=func_y_input_text_width,
                    default_value="sin(x)"
                )
                add_button(
                    label=build_der[self.lang],
                    callback=self.get_func_derivative,
                    width=build_der_width,
                    height=build_der_height
                )
            with group(horizontal=True, pos=[8, 724]):
                add_text(func_y_der[self.lang])
                self.func_der = add_input_text(
                    width=func_y_input_text_width,
                    default_value="cos(x)",
                    readonly=True
                )
            width, height, channels, data = load_image("images/cos.png")
            with group(pos=[8, 740], parent=self.derivative) as self.latex_group:
                with texture_registry() as self.formula_texture:
                    self.derivative_equation = add_static_texture(
                        width=width,
                        height=height,
                        default_value=data,
                    )
                with drawlist(width=760, height=100) as self.draw_list:
                    self.center_width, self.center_height = (760 // 2, 100 // 2)
                    draw_image(
                        texture_tag=self.derivative_equation,
                        pmin=(self.center_width - width // 1.5, self.center_height - height // 1.5),
                        pmax=(self.center_width + width // 1.5, self.center_height + height // 1.5),
                    )
            with group(horizontal=True, pos=[8, 850]):
                add_button(
                    label=TITLES["main_menu"][self.lang],
                    callback=main_menu.go_to_main_menu,
                    width=main_buttons_width
                )
                add_button(
                    label=TITLES["exit"][self.lang],
                    callback=self.close,
                    width=main_buttons_width
                )

    def get_derivative(self) -> int | str:
        return self.derivative

    @staticmethod
    def close() -> None:
        stop_dearpygui()

    def graphic_calculate_derivative(self, *, func_derivative: str) -> None:
        self.func_data_x, self.func_data_y = [], []
        x = int(get_value(self.min_x_der))
        # func_derivative: str = get_value(self.func_der).replace("**", "^")
        while x <= int(get_value(self.max_x_der)):
            data_y = calculate_graphs(
                    equation=func_derivative,
                    x=x
                )
            if isinstance(data_y, Float | Zero | int):
                self.func_data_x.append(x)
                self.func_data_y.append(data_y)
            x += 0.1
            set_value("graphic_of_func_der", [self.func_data_x, self.func_data_y])
            set_item_label("graphic_of_func_der", get_value(self.func_der))
        if get_value(self.choose_x_y_der) == choose_x_y_radio_text[self.lang][0]:
            set_axis_limits("x_axis_der", min(self.func_data_x), max(self.func_data_x))
            set_axis_limits("y_axis_der", min(self.func_data_y), max(self.func_data_y))
        if get_value(self.choose_x_y_der) == choose_x_y_radio_text[self.lang][1]:
            set_axis_limits("x_axis_der", int(get_value(self.min_x_der)), int(get_value(self.max_x_der)))
            set_axis_limits("y_axis_der", int(get_value(self.min_y_der)), int(get_value(self.max_y_der)))
        if get_value(self.choose_x_y_der) == choose_x_y_radio_text[self.lang][2]:
            set_axis_limits_auto("x_axis_der")
            set_axis_limits_auto("y_axis_der")
    
    def get_func_derivative(self) -> None:
        async def _insert_result_into_func_der(derivative: str) -> None:
            derivative = str(derivative).replace("**", "^")
            set_value(self.func_der, derivative)
            self.graphic_calculate_derivative(func_derivative=derivative)

        async def _get_latex_equation_image(derivative) -> None:
            equation_image: GetLatexEquationImage = await GetLatexEquationImage(equation=derivative)
            #print(f"{equation_image.get_formula_latex()=}")
            _load_new_png_parameters()

        def _load_new_png_parameters() -> None:
            width, height, channels, data = load_image("images/formula.png")
            #print(f"before: {width=}, {height=}")
            delete_item(self.formula_texture)
            delete_item(self.draw_list)
            _insert_image_into_draw_list(
                width=width,
                height=height,
                data=data
            )

        def _insert_image_into_draw_list(*, width: int, height: int, data: list[float] | tuple[float, ...]) -> None:
            coefficient = 1.8
            divider = 2
            while True:
                backup_width = width
                backup_height = height
                #print(f"after: {backup_width=}, {backup_height=}, {divider=}")
                backup_width //= divider
                backup_height //= divider
                #print(f"after: {backup_width=}, {backup_height=}, {divider=}")
                if backup_width <= self.draw_list_width and backup_height <= self.draw_list_height:
                    break
                divider += 1
            #print(f"after: {backup_width=}, {backup_height=}, {divider=}")
            with group(pos=[8, 750], parent=self.derivative):
                with texture_registry() as self.formula_texture:
                    self.derivative_equation = add_static_texture(
                        width=width,
                        height=height,
                        default_value=data,
                    )
                with drawlist(
                        width=self.draw_list_width,
                        height=self.draw_list_height
                ) as self.draw_list:
                    self.center_width, self.center_height = (
                        self.draw_list_width // 2,
                        self.draw_list_height // 2
                    )
                    draw_image(
                        texture_tag=self.derivative_equation,
                        pmin=(
                            self.center_width - width // (divider * coefficient),
                            self.center_height - height // (divider * coefficient)
                        ),
                        pmax=(
                            self.center_width + width // (divider * coefficient),
                            self.center_height + height // (divider * coefficient)
                        ),
                    )

        async def _main_() -> None:
            derivative = diff(get_value(self.func_to_der), 'x')
            await gather(
                _insert_result_into_func_der(derivative),
                _get_latex_equation_image(derivative)
            )
        run(_main_())
