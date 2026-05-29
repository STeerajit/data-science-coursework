# Python LLM Starter

_Development Environment Setup with pyenv, venv, direnv, Jupyter, and VS Code_

This repository provides a clean and maintainable Python project setup for working with large language models (LLMs), fine-tuning, Jupyter notebooks, and modern development workflows on macOS.

---

## Prerequisites

- macOS with Homebrew installed
- Visual Studio Code (recommended)
- Basic command-line experience

---

## 1. Install Required Tools

Install `pyenv` and `direnv` (once per machine):

```bash
brew install pyenv direnv
```

Append the following to your shell config (`~/.zshrc` or `~/.bashrc`):

```bash
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# direnv
eval "$(direnv hook zsh)"
```

Then reload your shell:

```bash
source ~/.zshrc
```

---

## 2. Initialize a New Project

```bash
cd /path/to/project

# Install Python 3.11.9 (if not already installed)
pyenv install 3.11.9

# Set Python version for the project
pyenv local 3.11.9

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

---

## 3. Install Dependencies

Install Python packages:

```bash
pip install -r requirements.txt
```

If you add new packages later, update the file:

```bash
pip freeze > requirements.txt
```

---

## 4. Enable direnv for Auto-Activation

Create a `.envrc` file:

```bash
echo 'layout python' > .envrc
direnv allow
```

This enables automatic activation of `.venv` whenever you enter the project folder.

---

## 5. Register Jupyter Kernel

To use this environment in Jupyter notebooks or VS Code:

```bash
python -m ipykernel install --user --name=myproject-env --display-name "Python (myproject)"
```

This ensures that the virtual environment appears as a selectable kernel.

---

## 6. Configure VS Code

In VS Code:

1. Open the command palette: `Cmd + Shift + P`
2. Select: `Python: Select Interpreter`
3. Choose `.venv/bin/python` or `"Python (myproject)"`

Alternatively, create `.vscode/settings.json`:

```json
{
  "python.pythonPath": ".venv/bin/python",
  "python.venvPath": "${workspaceFolder}/.venv",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

---

## 7. Run Jupyter Notebook

**Option 1: Terminal**

```bash
jupyter notebook
```

**Option 2: Visual Studio Code**

- Open a `.ipynb` file
- Select kernel: `Python (myproject)`

---

## Project Structure

```text
.venv/                 Virtual environment
.envrc                 direnv configuration
requirements.txt       Python dependencies
.vscode/settings.json  VS Code interpreter settings
main.ipynb             Example Jupyter notebook
main.py                Python script (optional)
```

---

## Usage

To run a script:

```bash
python main.py
```

To work with notebooks:

```bash
jupyter notebook
```

---

## License

This project is provided for educational and development purposes. Customize as needed for your organization or coursework.
