from re import search


samples = [
    "(-123)¹²³",
    "123¹²³",
    "¹²³√152",
    "¹²³√(-152)",
    "(¹²³√(-152) + ¹²³√(-152))",
    "(123¹²³ + 123¹²³)",
    "((-123)¹²³ + (-123)¹²³)"

]

for sample in samples:
    some = search(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+√[()\d-]+|(\(-)?\d+\)?[⁰¹²³⁴⁵⁶⁷⁸⁹]+", sample)
    if some:
        print(some.group())

print()

for sample in samples:
    some = search(r"(\(-)?\d+\)?[⁰¹²³⁴⁵⁶⁷⁸⁹]+", sample)
    if some:
        print(some.group())






"""|^[()\d-]*[⁰¹²³⁴⁵⁶⁷⁸⁹]*"""