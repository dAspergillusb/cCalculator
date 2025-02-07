from requests import get, Response
from requests.exceptions import ConnectionError as ErrorOfConnection
from os import path, mkdir
from sympy import (
    latex,
    sin,
    sinh,
    asin,
    asinh,
    cos,
    cosh,
    acos,
    acosh,
    tan,
    tanh,
    atan,
    atanh,
    log
)
from sympy.abc import x
from sympy.tensor.array.array_derivatives import ArrayDerivative, Derivative


class GetLatexEquationImage:

    def __init__(self, equation: ArrayDerivative | Derivative):
        self.formula_latex = ""
        self.status_code = None
        self.status_code, connection_good = self._is_connection_good()
        if connection_good:
            self.formula_latex = latex(equation)
            self._create_formula_latex_request_string()
        else:
            self._error_with_access()
        # print(self.formula_latex)

    def __await__(self):
        while self.status_code is None:
            yield None
        return self

    def _is_connection_good(self) -> tuple[int, bool] | None:
        try:
            request_: Response = get("https://latex.codecogs.com")
        except ErrorOfConnection:
            self._error_with_access()
            return 11001, False
        if request_.status_code == 200:
            return 200, True
        return request_.status_code, False

    def get_formula_latex(self):
        return self.formula_latex

    def _create_formula_latex_request_string(self):
        get_equation_string: str = (
                r"https://latex.codecogs.com/png.image?\dpi{300}&space;{\color{White}" +
                fr"{self.formula_latex}" +
                "}"
        )
        return self._get_image_from_latex_string(get_equation_string)

    def _get_image_from_latex_string(self, get_equation_string: str):
        image_bytecode_get: Response = get(get_equation_string)
        return self._create_png_file_from_bytecode(image_bytecode_get.content)

    @staticmethod
    def _create_png_file_from_bytecode(image_bytecode: bytes) -> None:
        if not path.exists("images"):
            mkdir("images")
        with open("images/formula.png", "wb") as formula_image:
            formula_image.write(image_bytecode)

    @staticmethod
    def _error_with_access():
        with open("images/connection_error.png", "rb") as bad_connection:
            message_bad_connection: bytes = bad_connection.read()
        with open("images/formula.png", "wb") as formula_image:
            formula_image.write(
                message_bad_connection
                )
