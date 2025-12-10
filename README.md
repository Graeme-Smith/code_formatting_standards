# GOSH Code Formatting Configuration

This repository contains VS Code configuration files and tooling standards for the GOSH Bioinformatics team. The primary goals are:

- **Standardise** formatting and tooling across all team members
- **Streamline** onboarding of new team members
- **Reduce** setup time for new Python projects

## Features, Team Standards & PEP8 Deviations

- **Fast Tooling**: Ruff for linting, formatting, and import sorting
- **Type Checking**: Pylance/Pyright integration with configurable strictness levels

The following standards were agreed as 'in-house' conventions after consultation with team members:

- **Line length**: Maximum 120 characters (vs PEP8's 79)
- **Docstring style**: Google format (vs PEP257's reStructuredText)
- **Type hints**: Gradual adoption encouraged, especially for public APIs
- **Import organization**: Alphabetical sorting with Ruff (vs PEP8's group imports by type: stdlib, third-party, local)

## Getting Started

### Option 1: Copy configuration to your existing project

Copy these files from this repository to your project:

- **`.vscode/settings.json`**
- **`.vscode/extensions.json`**
- **`pyproject.toml`**
- **`.editorconfig`**
- **`.gitignore`**

**Note**: For `pyproject.toml`, copy only the `[tool.ruff]`, `[tool.ruff.lint]`, `[tool.ruff.format]`, `[tool.mypy]`, `[tool.pyright]`, and `[tool.pytest.ini_options]` sections to avoid overwriting your project dependencies.

### Option 2: Use as a project template

```bash
# Clone this repository as your starting point
git clone https://github.com/gosh-team/code-formatting.git your-new-project
cd your-new-project

# Update project name (see TEMPLATE_SETUP.md)
PROJECT_NAME="your-project-name"
sed -i "s/project-template/$PROJECT_NAME/g" pyproject.toml
```

## Using the Tools in VS Code

### Essential VS Code Extensions (Auto-recommended)

When you open a project with these configs, VS Code will suggest installing:

- **Python** (`ms-python.python`) – Core Python support
- **Ruff** (`charliermarsh.ruff`) – Fast linting and formatting
- **Pylance** (`ms-python.vscode-pylance`) – Advanced Python language features
- **MyPy** (`ms-python.mypy-type-checker`) – Type checking integration

### Automatic Formatting

- **Format on Save**: Enabled automatically – your code formats when you save
- **Format Document**: `Shift+Alt+F` or right-click → **Format Document**
- **Format Selection**: Select code and use `Ctrl+K Ctrl+F`

### Code Quality Integration

- **Problems Panel**: `Ctrl+Shift+M` shows linting errors and warnings
- **Quick Fixes**: `Ctrl+.` on underlined code for automatic fixes
- **Organize Imports**: `Shift+Alt+O` sorts and removes unused imports
- **Type Checking**: Inline type errors shown as red squiggles

### Running Code & Debugging

- **Run Current File**: `F5` with the "Run Current File" configuration
- **Debug Mode**: Set breakpoints (`F9`) and press `F5` to debug
- **Integrated Terminal**: `Ctrl+` (backtick) opens a terminal with the selected Python environment

### Command Palette Quick Actions

Press `Ctrl+Shift+P` and type:

- **"Python: Select Interpreter"** – Choose your virtual environment
- **"Ruff: Format Document"** – Manual formatting
- **"Python: Run Tests"** – Execute pytest

### Configuring Pyright Typing Strictness

Pyright is configured via the `[tool.pyright]` section in `pyproject.toml`.

- **Default**: `typeCheckingMode = "basic"` with a moderate set of diagnostics enabled.
- **Stricter typing** (per-project or per-repo):

  1. Change in `pyproject.toml`:

     ```toml
     [tool.pyright]
     typeCheckingMode = "strict"
     ```

  2. Optionally uncomment/enable additional `report*` rules in the same section for even tighter checks (e.g. `reportMissingTypeStubs`, `reportUnused*`, `reportImplicitOverride`, etc.).

You can also override Pyright settings per workspace using `pyrightconfig.json` if you need different strictness for a specific project or directory.

## Command Line Usage

From the project root (with `pyproject.toml`):

- **Format & lint & type-check** (recommended):

  ```bash
  ruff format . && ruff check . --fix && pyright
  ```

- **Lint & type-check only**:

  ```bash
  ruff check . && pyright
  ```

- **Lint only**:

  ```bash
  ruff check . --fix
  ```

Run tests with coverage:

```bash
pytest
```

## Customisation

- Adjust **Python version**, **line length**, and **excluded paths** in `pyproject.toml` as needed.
- Update `[project]` metadata (name, description, authors) for your specific service or analysis pipeline.
- Teams may extend Ruff/Pyright rules locally, but core conventions (line length, docstrings, imports) should remain aligned with this template to maximise consistency across the GOSH Bioinformatics codebase.

Notes
Excluding sections from formatting

If you need to keep a small section of code exactly as written (e.g. alignment-sensitive output or embedded templates), you can disable the formatter with pragmas: add # fmt: off before the block and # fmt: on after it.

Import sorting

The formatter will not move deliberately placed mid-file imports to the top of the file. Ruff can normalise and sort existing import blocks, but it respects execution order and will not reorder statements in a way that changes runtime behaviour.

Formatter safety

The Ruff formatter is AST-safe: it does not change the underlying abstract syntax tree of your code. Formatting only affects presentation (whitespace, line breaks, quote style), not semantics, so running the code before and after formatting will produce the same results.
