# GOSH Code Formatting Configuration

This repository contains VS Code configuration files and tooling standards for the GOSH Bioinformatics team. The primary goals are:

* **Standardise** formatting and tooling across all team members
* **Streamline** onboarding of new team members
* **Reduce** setup time for new Python projects

## Features, Team Standards & PEP8 Deviations
* **Fast Tooling**: Ruff for linting, formatting, and import sorting
* **Type Checking**: Pylance/Pyright integration with configurable strictness levels
The following standards were agreed as 'in-house' conventions after consultation with team members:
* **Line length**: Maximum 120 characters (vs PEP8's 79)
* **Docstring style**: Google format (vs PEP257's reStructuredText)
* **Type hints**: Gradual adoption encouraged, required for public APIs
* **Import organization**: Alphabetical sorting with Ruff (vs PEP8's group imports by type (stdlib, third-party, local))

## Getting Started

**Option 1: Copy configuration to your existing project**

Copy these files from this repository to your project:

* **`.vscode/settings.json`**
* **`.vscode/extensions.json`** 
* **`pyproject.toml`**
* **`.editorconfig`**
* **`.gitignore`**

**Note**: For `pyproject.toml`, copy only the `[tool.ruff]`, `[tool.ruff.lint]`, `[tool.ruff.format]`, `[tool.mypy]`, `[tool.pyright]`, and `[tool.pytest.ini_options]` sections to avoid overwriting your project dependencies.

**Option 2: Use as a project template**
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

* **Python** (`ms-python.python`) - Core Python support
* **Ruff** (`charliermarsh.ruff`) - Fast linting and formatting  
* **Pylance** (`ms-python.vscode-pylance`) - Advanced Python language features
* **MyPy** (`ms-python.mypy-type-checker`) - Type checking integration

### Automatic Formatting
* **Format on Save**: Enabled automatically - your code formats when you save
* **Format Document**: `Shift+Alt+F` or right-click → "Format Document"
* **Format Selection**: Select code and use `Ctrl+K Ctrl+F`

### Code Quality Integration
* **Problems Panel**: `Ctrl+Shift+M` shows linting errors and warnings
* **Quick Fixes**: `Ctrl+.` on underlined code for automatic fixes
* **Organize Imports**: `Shift+Alt+O` sorts and removes unused imports
* **Type Checking**: Inline type errors shown as red squiggles

### Running Code & Debugging
* **Run Current File**: `F5` with "Run Current File" configuration
* **Debug Mode**: Set breakpoints (F9) and press F5 to debug
* **Integrated Terminal**: `Ctrl+`` opens terminal with proper Python environment

### Command Palette Quick Actions
Press `Ctrl+Shift+P` and type:
* **"Python: Select Interpreter"** - Choose your virtual environment
* **"Ruff: Format Document"** - Manual formatting  
* **"Python: Run Tests"** - Execute pytest
* **"MyPy: Run Type Checking"** - Manual type check

### Configuring Pyright Typing Strictness

The `pyproject.toml` includes three two strictness levels. Choose based on your project's needs:

### Level 1: Permissive (Default)
```toml
disallow_untyped_defs = false    # Functions can have no type hints
ignore_missing_imports = true    # Ignore libraries without stubs
```
**Good for**: Existing codebases, gradual type hint adoption

### Level 2: Moderate (Recommended for GOSH)
```toml
disallow_untyped_defs = true      # Function signatures must have types
disallow_incomplete_defs = true   # All parameters must be typed
ignore_missing_imports = true     # Still forgiving with libraries
```
**Good for**: Teams adopting type hints, bioinformatics projects with many dependencies

### Level 3: Strict
```toml
strict = true                     # All strict checks enabled
```
**Good for**: New projects, teams with strong typing discipline

### How to Change Strictness

1. **Open `pyproject.toml`**
2. **Find the `[tool.mypy]` section**
3. **Comment out current level** (add `#` at line start)
4. **Uncomment desired level** (remove `#`)
5. **Run MyPy** to see current issues: `mypy src/`

