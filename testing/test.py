from re import search
from time import perf_counter
from timeit import timeit
from math import sin, cos, tan, log
from sympy import simplify


def equation_parsing(*, equation_: str, x: float) -> float:
    """
    Function parsing equation_ as string, calculate the sin, cos, tan..., and insert result of calculation in equation_.
    Then it calculates equating with value of "x"
    :param equation_: Equation string with variable "x".
    :param x: What the value of variable "x" is.
    :return: Calculation result of equation as float value.
    """
    while replaces_ := search(r"a?[sctl][ioa][nsg]h?\d?\d?[(][ ()x\d^+*/-]*[)]", equation_):
        replaces_ = replaces_.group()
        if replaces_.count(")") > replaces_.count("("):
            count_open_parenthesis: int = replaces_.count("(")
            count_close_parenthesis: int = replaces_.count(")")
            replaces_ = replaces_[:count_open_parenthesis - count_close_parenthesis]
        function_literal: str = replaces_[:replaces_.index("(")]
        function_argument: str = replaces_[replaces_.index("(") + 1:replaces_.rindex(")")]
        function_argument = simplify(function_argument.replace("x", f"{x}"))
        function_result: float = globals()[function_literal](function_argument)
        if function_result < 0:
            equation_ = equation_.replace(replaces_, f"({function_result})")
        else:
            equation_ = equation_.replace(replaces_, f"{function_result}")
    if x < 0:
        equation_ = equation_.replace("x", f"({x})")
    else:
        equation_ = equation_.replace("x", f"{x}")
    return simplify(equation_)


equation_one = "log(x)"
# print(timeit(equation_parsing, number=1000))
time_start = perf_counter()
list_x = [x / 10 for x in range(-10, 11)]
list_y = []
for x in list_x:
    list_y.append(
        equation_parsing(
            equation_=equation_one,
            x=x
        )
    )
print(f"time needed: {perf_counter() - time_start:0.3f} seconds")
print(list_y)
