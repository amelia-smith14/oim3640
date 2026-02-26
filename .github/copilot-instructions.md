# AI Coding Agent Instructions for OIM3640

## Project Overview
This is an **OIM3640 Spring 2026 course repository** for a Business Analytics student. The project focuses on learning Python fundamentals and building a practical application: a **grade calculator** that helps students compute course grades and potential GPA impacts.

## Project Structure & Key Directories

- **`/code`** - Foundational Python learning scripts (hello.py, calc.py, recursive.py, s*.py files)
- **`/notebooks`** - Jupyter notebooks (chap00-chap19.ipynb) following "Think Python" curriculum with helper utilities
- **`/projects`** - Course projects, primary focus is `miniproject1.py` (grade calculator)
- **`/logs`** - Session notes (s01.md, s02.md, etc.) documenting weekly learning and challenges
- **`/data`** - Data files (currently empty, for future use)

## Core Application: Grade Calculator

**Location:** [projects/miniproject1.py](projects/miniproject1.py)

**Purpose:** Calculate weighted course grades and explore how different assignment results impact final grades.

**Current Implementation:**
- Accepts assignment name, grade (0-100), and weight (as percentage)
- Calculates weighted sum across all assignments
- Returns current course grade and total weight percentage
- Uses interactive `while` loop for user input until 'done' is entered

**Planned Enhancements (from [PROPOSAL.md](logs/PROPOSAL.md)):**
- Support for previous course grades and credit hours for GPA calculation
- Grade requirement calculator (what grade needed for target letter grade)
- Multiple loops and control flow handling

## Development Patterns & Conventions

### Python Style
- Beginner-level Python with focus on core language fundamentals
- Use of `input()` for interactive CLI input
- Simple function-based structure without classes (currently)
- Comments in code reflect learning objectives, not production practices

### Jupyter Notebook Usage
- **Notebooks** in `/notebooks` are learning materials, not primary deliverables
- **Helper modules:**
  - `thinkpython.py` - Provides cell magic for "Think Python" curriculum (function extraction, cell routing)
  - `jupyturtle.py` - Graphics/turtle graphics support for visualization assignments
- Notebooks reference "Think Python Third Edition" curriculum framework

### Testing & Execution
- Code in `/code` is primarily for practice exercises
- Run Python files directly: `python filename.py`
- Interactive scripts expect user input via terminal
- No automated test framework in use

## Development Workflow Notes

### Interactive Development
- Primary workflow is script execution in VS Code terminal or Python terminal
- Use `input()` prompts for CLI interaction
- Print statements for output verification

### Session Documentation
- Track learning and challenges in `/logs/s##.md` files (weekly reflections)
- Document issues, questions, and AI usage in session notes
- Cross-reference code work with session documentation

### Common Pain Points (from session notes)
- Prompt engineering uncertainty when using AI tools
- Multiple nested loops and control flow complexity
- Environment/IDE selection for running Python code
- Understanding how quick-prototyped solutions integrate into larger projects

## When Helping with This Project

1. **Grade Calculator enhancements**: Focus on input validation, weighted calculations, and clear output formatting
2. **Learning context**: Treat code as educational—explain fundamentals, not just provide solutions
3. **Integration**: When extending features, maintain simple function structure without premature class design
4. **Error handling**: Add input validation (valid grades 0-100, weights as valid percentages) with user-friendly messages
5. **Testing ideas**: Suggest test cases but keep execution manual/interactive to match current workflow

## External Dependencies

- **Python 3.x** (standard library only for `/code` and `/projects`)
- **Jupyter** with IPython (for notebook environment)
- **jupyturtle** and **thinkpython** modules (local utilities in `/notebooks` directory, learning-focused)

---

**Last updated:** February 2026 | **Project Phase:** Active development of Grade Calculator (miniproject1)
