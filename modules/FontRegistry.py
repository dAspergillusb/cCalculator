from dearpygui.dearpygui import (
    font_registry,
    font,
    add_font_range_hint,
    mvFontRangeHint_Cyrillic,
    add_font_chars
)
from modules.font_chars import CHARS_INT


class FontRegistry:

    def __init__(self):
        with font_registry():
            with font("font/calibri_bold.ttf", 22, default_font=True) as self.font_header:
                add_font_range_hint(mvFontRangeHint_Cyrillic)
            with font("font/calibri_bold.ttf", 20, default_font=True) as self.font_calculator:
                add_font_range_hint(mvFontRangeHint_Cyrillic)
                add_font_chars(CHARS_INT)
            with font("font/calibri.ttf", 16, default_font=True) as self.font_common:
                add_font_range_hint(mvFontRangeHint_Cyrillic)
                add_font_chars(CHARS_INT)
            with font("font/calibri_bold.ttf", 14, default_font=True) as self.font_axis:
                add_font_range_hint(mvFontRangeHint_Cyrillic)
            with font("font/calibri.ttf", 8, default_font=True) as self.font_num_sys_arith:
                add_font_range_hint(mvFontRangeHint_Cyrillic)

    def get_font_header(self):
        return self.font_header

    def get_font_calculator(self):
        return self.font_calculator

    def get_font_common(self):
        return self.font_common

    def get_font_axis(self):
        return self.font_axis

    def get_font_num_sys_arith(self):
        return self.font_num_sys_arith
