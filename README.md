# commentclip

A command-line tool for extracting comments from source code files. Supports multiple programming languages and output formats.

## Features

- Extract comments from various programming languages
- Support for single-line, multi-line, and docstring comments
- Multiple output formats (text, JSON)
- Line number information
- Comment type filtering
- Language auto-detection based on file extensions

## Supported Languages

- **Python** (`.py`) - `#` comments and `"""` / `'''` docstrings
- **JavaScript/TypeScript** (`.js`, `.jsx`, `.ts`, `.tsx`) - `//` and `/* */` comments
- **Java** (`.java`) - `//` and `/* */` comments
- **C/C++** (`.c`, `.h`, `.cpp`, `.hpp`, `.cc`, `.cxx`) - `//` and `/* */` comments
- **Go** (`.go`) - `//` and `/* */` comments
- **Rust** (`.rs`) - `//` and `/* */` comments
- **HTML** (`.html`, `.htm`) - `<!-- -->` comments
- **CSS** (`.css`, `.scss`, `.sass`) - `/* */` comments
- **Shell** (`.sh`, `.bash`, `.zsh`) - `#` comments
- **Ruby** (`.rb`) - `#` and `=begin`/`=end` comments
- **PHP** (`.php`) - `//`, `/* */`, and `#` comments

## Installation

### From source
```bash
git clone https://github.com/osyoooo/commentclip.git
cd commentclip
python setup.py install
```

### Direct usage
```bash
python commentclip.py [options] <files...>
```

## Usage

### Basic usage
```bash
commentclip file.py
```

### Extract comments from multiple files
```bash
commentclip *.py *.js
```

### JSON output format
```bash
commentclip --format json file.py
```

### Include line numbers
```bash
commentclip --line-numbers file.py
```

### Filter by comment type
```bash
# Only docstrings
commentclip --type docstring *.py

# Only single-line comments
commentclip --type single-line *.js

# Only multi-line comments
commentclip --type multi-line *.c
```

### Override language detection
```bash
commentclip --language python some_file_without_extension
```

## Output Examples

### Text format (default)
```
=== example.py (python) ===
Total comments: 3

[DOCSTRING]
This is a module docstring.
It describes what the module does.

[SINGLE-LINE]
This is a single-line comment

[SINGLE-LINE]
Another comment here
```

### JSON format
```json
[
  {
    "file": "example.py",
    "language": "python",
    "comments": [
      {
        "text": "This is a module docstring.\nIt describes what the module does.",
        "start_line": 1,
        "end_line": 4,
        "raw": "\"\"\"\nThis is a module docstring.\nIt describes what the module does.\n\"\"\"",
        "type": "docstring"
      }
    ],
    "total_comments": 1
  }
]
```

## Command Line Options

- `files`: Source code files to process (supports glob patterns)
- `--format {text,json}`: Output format (default: text)
- `--line-numbers`: Include line numbers in output
- `--type {single-line,multi-line,docstring}`: Filter comments by type
- `--language LANGUAGE`: Override automatic language detection

## Use Cases

- **Documentation extraction**: Extract docstrings and comments for documentation generation
- **Code review**: Quickly review all comments in a codebase
- **Comment analysis**: Analyze comment patterns and density in projects
- **Migration assistance**: Extract comments when porting code between languages
- **Quality assurance**: Ensure code has adequate commenting

## License

MIT License