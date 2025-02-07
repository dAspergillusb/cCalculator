from os import name

match name:
    case "posix":
        windows_width = {
            "main_menu": 300,
            "numerical_system": 650,
            "numerical_system_arithmetic": 564,
            "calculator": 508,
            "graphics": 1000,
            "derivative": 800
        }
        windows_height = {
            "main_menu": 235,
            "numerical_system": 210,
            "numerical_system_arithmetic": 494,
            "calculator": 410,
            "graphics": 790,
            "derivative": 884
        }
    case "nt":
        windows_width = {
            "main_menu": 300,
            "numerical_system": 654,
            "numerical_system_arithmetic": 580,
            "calculator": 524,
            "graphics": 1010,
            "derivative": 812
        }
        windows_height = {
            "main_menu": 280,
            "numerical_system": 248,
            "numerical_system_arithmetic": 530,
            "calculator": 450,
            "graphics": 820,
            "derivative": 920
        }
