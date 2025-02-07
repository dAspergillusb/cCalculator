from tkinter import Tk
from dearpygui.dearpygui import (
    set_viewport_large_icon,
    set_viewport_small_icon,
    create_context,
    create_viewport,
    configure_viewport,
    bind_theme,
    set_primary_window,
    bind_font,
    setup_dearpygui,
    show_viewport,
    start_dearpygui,
    destroy_context,
    set_viewport_title
)
from modules.Exceptions import WrongLanguageInConfig
from modules.Themes import Themes
from modules.FontRegistry import FontRegistry
from modules.windows_parameters import (
    windows_width,
    windows_height,
)
from modules.MainMenu import MainMenu
from modules.main_config import TITLES


RU_LANG_NUMBER: int = 0
EN_LANG_NUMBER: int = 1
LANGUAGES: dict = {
    "ru": RU_LANG_NUMBER,
    "en": EN_LANG_NUMBER
}


def get_resolution() -> tuple[int, int]:
    desktop_area = Tk()
    return desktop_area.winfo_screenwidth(), desktop_area.winfo_screenheight()


def get_language() -> int | None:
    with open("lang/language", "r") as language:
        lang_strings = [string.strip("\n") for string in language.readlines()]
    for lang in lang_strings:
        if lang in LANGUAGES:
            return LANGUAGES[lang]


def main() -> None:
    resolution_width, resolution_height = get_resolution()
    viewport_x_pos = resolution_width // 2 - windows_width["main_menu"] // 2
    viewport_y_pos = resolution_height // 2 - windows_height["main_menu"] // 2
    language = get_language()
    if isinstance(language, int):
        lang = language
    else:
        raise WrongLanguageInConfig(
            "Wrong parameter in language config file at \"lang/language\". Is is should be \"ru\" or \"en\"."
        )
    title: str = TITLES["main_title"][lang]
    title_upper_frame: bytes = title.encode(encoding="1251")
    create_context()
    create_viewport(
        large_icon="icon.ico",
        small_icon="icon.ico",
        decorated=True,
    )
    set_viewport_title(title)
    configure_viewport(
        item=0,
        x_pos=viewport_x_pos,
        y_pos=viewport_y_pos,
        width=windows_width.get("main_menu"),
        height=windows_height.get("main_menu")
    )
    themes = Themes()
    font = FontRegistry()
    main_menu = MainMenu(
        lang=lang,
        title=title,
        font=font,
        themes=themes,
        resolution=(resolution_width, resolution_height)
    )
    bind_theme(themes.get_global_theme())
    set_primary_window(
        window=main_menu.get_main_menu(),
        value=True,
    )
    bind_font(font.get_font_common())
    setup_dearpygui()
    show_viewport()
    start_dearpygui()
    destroy_context()


if __name__ == '__main__':
    main()
