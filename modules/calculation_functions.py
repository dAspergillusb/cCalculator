from re import search
from operator import truediv
from sympy import simplify, nsimplify
from math import (
    log,
    log2,
    log10,
    factorial,
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
    pow,
    ceil
)
from modules.font_chars import (
    CHARS_INT,
    CHARS_DICT_SUPERSCRIPT
)


CHARS_CHR = [
    chr(char) for char in CHARS_INT
]


def calculate_graphs(*, equation: str, x: float) -> float | None:
    """
    Function parsing equation_ as string, calculate the sin, cos, tan..., and insert result of calculation in equation_.
    Then it calculates equation with value of "x"
    :param equation: Equation string with variable "x".
    :param x: What the value of variable "x" is.
    :return: Calculation result of equation as float value.
    """
    while replaces_ := search(r"(a?[sctl][ioa][nsg]h?\d?\d?)|[ x*/+\d()-]+!", equation):
        # Define the name of function
        function_literal: str = replaces_.group()
        if "!" in function_literal:
            try:
                function_result = factorial(nsimplify(function_literal[:-1].replace("x", f"{int(x)}")))
            except ValueError:
                return None
            return function_result

        # Split the function at "function_literal" and "function_argument"
        start_index_function_literal: int = equation.index(function_literal[-1]) + 2
        function_argument: str = "("
        open_parenthesis_count: int = function_argument.count("(")
        close_parenthesis_count: int = function_argument.count(")")

        # Trying to understand the size of function argument
        while open_parenthesis_count != close_parenthesis_count:
            function_argument += equation[start_index_function_literal]
            start_index_function_literal += 1
            open_parenthesis_count = function_argument.count("(")
            close_parenthesis_count = function_argument.count(")")

        full_function: str = function_literal + function_argument
        function_argument = simplify(function_argument.replace("x", f"({x})"))

        # Calculating the value of function
        try:
            function_result: float = globals()[function_literal](function_argument)
        except ValueError:
            return None
        equation = equation.replace(full_function, f"({function_result})")
    equation = equation.replace("x", f"({x})")
    return simplify(equation)


def calculate(expression: str, rational_fraction: bool = False, trigonometry_value: int | float = 1) -> float | int | str:
    """
    Function calculating the value of expression. Firs of all expression is parsed in fractions, and it is calculated
    separately. After all micro-calculations expression with values is sent to eval or nsimplify functions to calculate
    value of full expression.
    :param expression: It is string with formula that must be calculated.
    :param rational_fraction: Parameter that defines what view of calculated result will be inserted into answer area.
    It may be as decimal fraction (like 0.15, 1.56) or rational fraction (like 1/2, 2/5).
    :param trigonometry_value: Value, that define what of units of sine, cosine... arguments will be calculated.
    :return: Function returns calculated value of expression.
    """
    # Search any supported function like "sin(...) or cos(...) etc.
    while replaces_ := search(r"(a?[sctl][ioa][nsg]h?\d?\d?\()|!", expression):
        function_literal: str = replaces_.group()
        # Check if function is factorial
        if function_literal == "!":
            index_factorial_sign: int = expression.index("!")
            decimal_index: int = index_factorial_sign - 1
            decimal_list = []
            while decimal_index >= 0 and expression[decimal_index].isdecimal():
                decimal_list.append(expression[decimal_index])
                decimal_index -= 1
                if expression[decimal_index] == ".":
                    raise ValueError("Factorial takes only integers!")
            buffer_arg: str = "".join(decimal_list)
            factorial_result: int = factorial_(int(buffer_arg))
            expression = expression.replace(f"{buffer_arg}!", f"{factorial_result}")

        # Otherwise, if function any of supported functions
        if "(" in function_literal:
            start_function_arg: int = expression.index(function_literal[-2]) + 2
            # That is exactly index of any num after "(" sign.
            chars_list = ["("]
            while chars_list.count("(") > chars_list.count(")"):
                chars_list.append(expression[start_function_arg])
                start_function_arg += 1
            function_arg: str = "".join(chars_list)[1:-1]
            function_literal += f"{function_arg})"
            recursion_buffer_arg = None
            try:
                float(function_arg)
            except ValueError:
                recursion_buffer_arg = calculate(expression=function_arg, trigonometry_value=trigonometry_value)
            finally:
                recursion_buffer_arg = recursion_buffer_arg if recursion_buffer_arg else function_arg
                recursion_function_literal = function_literal.replace(function_arg, str(recursion_buffer_arg))
                expression = expression.replace(
                    f"{function_literal}",
                    f"{_calculate_non_decimal(f'{recursion_function_literal}', trigonometry_value)}")

    # Then we need to search any power function:
    while replaces_ := search(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+√[()\d-]+|(\(-)?\d+\)?[⁰¹²³⁴⁵⁶⁷⁸⁹]+", expression):
        function = replaces_.group()
        expression = expression.replace(function, f"({_calculate_power(function)})")

    # Finally, expression with numbers sends to eval or nsimplify function for calculation.
    expression = eval(expression)
    if rational_fraction:
        expression = str(nsimplify(expression))
        if "sqrt" in expression:
            expression = expression.replace("sqrt", f"{CHARS_CHR[2]}{CHARS_CHR[11]}")
    return expression


def _calculate_power(function: str) -> float | int:
    if CHARS_CHR[11] in function:
        for char in function[:function.index(CHARS_CHR[11])]:
            function = function.replace(char, CHARS_DICT_SUPERSCRIPT[char])
        function = function.replace(CHARS_CHR[11], " ")
        return radical_n(function)
    if (
            CHARS_CHR[0] in function or
            CHARS_CHR[1] in function or
            CHARS_CHR[2] in function or
            CHARS_CHR[3] in function or
            CHARS_CHR[4] in function or
            CHARS_CHR[5] in function or
            CHARS_CHR[6] in function or
            CHARS_CHR[7] in function or
            CHARS_CHR[8] in function or
            CHARS_CHR[9] in function
    ):
        min_index_: int = len(function) - 1
        min_index_ = min(
            [min(min_index_, index)
             if function[index] in CHARS_CHR else min_index_
             for index in range(len(function) - 1)])
        function = f"{function[:min_index_]}**{function[min_index_:]}"
        for char in function[function.index("**") + 2:]:
            function = function.replace(char, CHARS_DICT_SUPERSCRIPT[char])
        return power_xy(function)


def _calculate_non_decimal(function: str, trigonometry_value: int | float) -> int | float:
    function_literal: str = function[:function.index("(")]
    arg_of_function: float = simplify(function[function.index("(") + 1:-1])
    match function_literal:
        case "log":
            return log_nature(arg_of_function)
        case "log₂":
            return log_base_2(arg_of_function)
        case "log₁₀":
            return log_base_10(arg_of_function)
        case "sin":
            return sine(arg_of_function * trigonometry_value)
        case "sinh":
            return sine_hyperbolic(arg_of_function * trigonometry_value)
        case "asin":
            return arc_sine(arg_of_function) * trigonometry_value
        case "asinh":
            return arc_sine_hyperbolic(arg_of_function) * trigonometry_value
        case "cos":
            return cosine(arg_of_function * trigonometry_value)
        case "cosh":
            return cosine_hyperbolic(arg_of_function * trigonometry_value)
        case "acos":
            return arc_cosine(arg_of_function) * trigonometry_value
        case "acosh":
            return arc_cosine_hyperbolic(arg_of_function) * trigonometry_value
        case "tan":
            return tangent(arg_of_function * trigonometry_value)
        case "tanh":
            return tangent_hyperbolic(arg_of_function * trigonometry_value)
        case "atan":
            return arc_tangent(arg_of_function) * trigonometry_value
        case "atanh":
            return arc_tangent_hyperbolic(arg_of_function) * trigonometry_value
        case "cot":
            return cotangent(arg_of_function) * trigonometry_value


def _calculate_expression(calculated: str) -> float:
    arg_one, arg_two = calculated.split("/")
    return truediv(float(arg_one), float(arg_two))


def log_nature(arg_of_function: float) -> float:
    return log(arg_of_function)


def log_base_2(arg_of_function: float) -> float:
    return log2(arg_of_function)


def log_base_10(arg_of_function: float) -> float:
    return log10(arg_of_function)


def factorial_(arg_of_function: int) -> int:
    return factorial(arg_of_function)


def sine(arg_of_function: float) -> float:
    return sin(arg_of_function)


def sine_hyperbolic(arg_of_function: float) -> float:
    return sinh(arg_of_function)


def arc_sine(arg_of_function: float) -> float:
    return asin(arg_of_function)


def arc_sine_hyperbolic(arg_of_function: float) -> float:
    return asinh(arg_of_function)


def cosine(arg_of_function: float) -> float:
    return cos(arg_of_function)


def cosine_hyperbolic(arg_of_function: float) -> float:
    return cosh(arg_of_function)


def arc_cosine(arg_of_function: float) -> float:
    return acos(arg_of_function)


def arc_cosine_hyperbolic(arg_of_function: float) -> float:
    return acosh(arg_of_function)


def tangent(arg_of_function: float) -> float:
    return tan(arg_of_function)


def tangent_hyperbolic(arg_of_function: float) -> float:
    return tanh(arg_of_function)


def arc_tangent(arg_of_function: float) -> float:
    return atan(arg_of_function)


def arc_tangent_hyperbolic(arg_of_function: float) -> float:
    return atanh(arg_of_function)


def cotangent(arg_of_function: float) -> float:
    return cosine(arg_of_function) / sine(arg_of_function)


def sqrt(arg_of_function: float) -> float:
    return pow(arg_of_function, 1 / 2)


def radical3(arg_of_function: float) -> float:
    return pow(arg_of_function, 1 / 3)


def radical_n(arg_of_function: str) -> float:
    root_power, number = map(int, arg_of_function.split())
    return pow(number, 1 / root_power)


def power_xy(arg_of_function: str) -> float:
    number, power = map(int, arg_of_function.split("**"))
    return pow(number, power)


def square(arg_of_function: float | int) -> float | int:
    return pow(arg_of_function, 2)


if __name__ == '__main__':
    equation_one = "(-2*x*sin(x^2 + (x + 3) * (x + 165)) + cos(x))/tan(x) + (sin(x)^2 + cos(x^2))*(-tan(x)^2 - 1)/tan(x)^2"
    argument_one = -8
    equation_two = "log(x)"
    equation_three = "(cos(x) * sin(x^2 + 2 * x + 8)) * tan(15 * x)"
    # print(f"equation_one parsed string: {calculate_graphs(equation=equation_two,x=-8)}")
    """print("Start parsing equation two:", end="\n\n")
    print(f"equation_two parsed string: {calculate_graphs(
        equation=equation_two,
        argument=15
    )}"
          )
    print("Start parsing equation three:", end="\n\n")
    print(f"equation_three parsed string: {calculate_graphs(
        equation=equation_three,
        argument=18.8
    )}"
          )"""
    arg = "60"
    _equation = f"8!"
    #replaces = search(r"a?[sctl][ioa][nsg]h?\d?\d?|[ x*/+\d()-]+!", _equation)
    print(calculate(expression=_equation, trigonometry_value=(3.14 / 180)))
