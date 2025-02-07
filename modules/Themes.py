from dearpygui.dearpygui import (
    theme,
    theme_component,
    mvAll,
    add_theme_color,
    add_theme_style,
    mvThemeCol_FrameBg,
    mvStyleVar_FrameRounding,
    mvThemeCat_Core,
    mvInputInt,
    mvThemeCol_Button,
    mvThemeCol_Text
)


class Themes:
    
    def __init__(self):
        with theme(tag="plot_theme") as self.global_theme:
            with theme_component(mvAll):
                add_theme_color(mvThemeCol_FrameBg, (50, 50, 50), category=mvThemeCat_Core)
                add_theme_color(mvThemeCol_Button, (45, 45, 45, 200), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

            with theme_component(mvInputInt):
                add_theme_color(mvThemeCol_FrameBg, (0, 0, 139), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

        with theme() as self.disabled_theme:
            with theme_component(mvAll):
                add_theme_color(mvThemeCol_FrameBg, (80, 30, 30), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

            with theme_component(mvInputInt):
                add_theme_color(mvThemeCol_FrameBg, (0, 0, 139), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

        with theme() as self.shifted_theme:
            with theme_component(mvAll):
                add_theme_color(mvThemeCol_Button, (60, 20, 20, 200), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

        with theme() as self.default_button_theme:
            with theme_component(mvAll):
                add_theme_color(mvThemeCol_Button, (45, 45, 45, 200), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

        with theme() as self.disabled_button_theme:
            with theme_component(mvAll):
                add_theme_color(mvThemeCol_Button, (40, 40, 40, 200), category=mvThemeCat_Core)
                add_theme_color(mvThemeCol_Text, (45, 45, 45, 200), category=mvThemeCat_Core)
                add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)

    def get_global_theme(self):
        return self.global_theme

    def get_disabled_theme(self):
        return self.disabled_theme

    def get_shifted_theme(self):
        return self.shifted_theme

    def get_default_button_theme(self):
        return self.default_button_theme

    def get_disabled_button_theme(self):
        return self.disabled_button_theme
