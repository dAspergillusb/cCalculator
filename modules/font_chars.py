ZERO_SUPERSCRIPT: int = ord("⁰")
ONE_SUPERSCRIPT: int = ord("¹")
TWO_SUPERSCRIPT: int = ord("²")
THREE_SUPERSCRIPT: int = ord("³")
FOUR_SUPERSCRIPT: int = ord("⁴")
FIVE_SUPERSCRIPT: int = ord("⁵")
SIX_SUPERSCRIPT: int = ord("⁶")
SEVEN_SUPERSCRIPT: int = ord("⁷")
EIGHT_SUPERSCRIPT: int = ord("⁸")
NINE_SUPERSCRIPT: int = ord("⁹")
N_SUPERSCRIPT: int = ord("ⁿ")
ROOT_CHAR: int = ord("√")
ZERO_SUBSCRIPT: int = ord("₀")
ONE_SUBSCRIPT: int = ord("₁")
TWO_SUBSCRIPT: int = ord("₂")
THREE_SUBSCRIPT: int = ord("₃")
FOUR_SUBSCRIPT: int = ord("₄")
FIVE_SUBSCRIPT: int = ord("₅")
SIX_SUBSCRIPT: int = ord("₆")
SEVEN_SUBSCRIPT: int = ord("₇")
EIGHT_SUBSCRIPT: int = ord("₈")
NINE_SUBSCRIPT: int = ord("₉")

CHARS_INT: list[int] = [
    ZERO_SUPERSCRIPT,
    ONE_SUPERSCRIPT,
    TWO_SUPERSCRIPT,
    THREE_SUPERSCRIPT,
    FOUR_SUPERSCRIPT,
    FIVE_SUPERSCRIPT,
    SIX_SUPERSCRIPT,
    SEVEN_SUPERSCRIPT,
    EIGHT_SUPERSCRIPT,
    NINE_SUPERSCRIPT,
    N_SUPERSCRIPT,
    ROOT_CHAR,
    ZERO_SUBSCRIPT,
    ONE_SUBSCRIPT,
    TWO_SUBSCRIPT,
    THREE_SUBSCRIPT,
    FOUR_SUBSCRIPT,
    FIVE_SUBSCRIPT,
    SIX_SUBSCRIPT,
    SEVEN_SUBSCRIPT,
    EIGHT_SUBSCRIPT,
    NINE_SUBSCRIPT
]
CHARS_DICT_SUPERSCRIPT: dict[str: str] = {
    "⁰": "0",
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9"
}
CHARS_DICT_SUBSCRIPT: dict[str: str] = {
    "₀": "0",
    "₁": "1",
    "₂": "2",
    "₃": "3",
    "₄": "4",
    "₅": "5",
    "₆": "6",
    "₇": "7",
    "₈": "8",
    "₉": "9"
}
