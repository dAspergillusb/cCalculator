<p align="right">
  <a href="README.md">🇬🇧 English</a> |
  <a href="README.RU.md">🇷🇺 Русский</a>
</p>

# cCalculator

A modular Python desktop application that combines numerical calculations, numeral-system conversion, symbolic mathematics, and graphing in a graphical interface.

The project started as a learning application and evolved into a multi-tool desktop program built with **Python**, **Dear PyGui**, and **SymPy**.

## Features

- classic calculator
- numeral-system conversion up to base 36
- arithmetic operations between values represented in different numeral systems
- configurable output numeral system
- plotting of mathematical functions
- simultaneous graphing of multiple functions
- symbolic derivative calculation
- derivative graph generation
- LaTeX representation of symbolic results
- multilingual application resources
- modular project structure

## Tech Stack

- Python
- Dear PyGui
- SymPy
- Requests

## Project Structure

```text
.
├── main.py
├── modules/
├── testing/
├── images/
├── font/
├── lang/
├── requirements.txt
├── README.md
└── README.RU.md
```

The application is split into separate modules rather than keeping all calculator, graphing, and GUI logic in a single file. This project was one of my early exercises in structuring a larger Python application and separating responsibilities between components.

## Main Capabilities

### Classic Calculator

Provides standard arithmetic operations through the graphical interface.

### Numeral Systems

Converts numbers between numeral systems up to base 36.

The application also supports arithmetic operations where input values may use different numeral systems and the result can be returned in a selected target base.

### Function Graphing

Plots mathematical functions and supports displaying multiple graphs in the same working area.

### Symbolic Derivatives

Uses SymPy to calculate derivatives, display the symbolic result, render its LaTeX representation, and plot the resulting derivative function.

## Installation

Python **3.12+** is recommended for the current project version.

Clone the repository:

```bash
git clone https://github.com/dAspergillusb/cCalculator.git
cd cCalculator
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## What This Project Demonstrates

This project reflects practical experience with:

- structuring a multi-module Python application
- desktop GUI development
- event-driven application logic
- mathematical expression processing
- symbolic computation
- graph generation
- data conversion and validation
- working with third-party Python libraries

## Project Context

`cCalculator` was one of my first larger Python projects. I keep it public because it shows the progression from basic Python exercises toward modular application development and more complex backend/web projects in my current portfolio.

## Author

**Nikita Zelentsov**  
Python Backend Developer

GitHub: [@dAspergillusb](https://github.com/dAspergillusb)

## License

GNU GPL v3
