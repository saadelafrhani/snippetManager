from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from pygments.token import Comment, Name, Text

class CustomFormatter:
    def __init__(self):
        self.highlighted_code = ""

    def format(self, tokensource):
        for ttype, value in tokensource:
            if ttype in (Comment, Name):
                # Change comment color to green
                self.highlighted_code += f"\033[92m{value}\033[0m"  # ANSI escape code for green
            else:
                self.highlighted_code += value

def apply_syntax_highlighting(self):
    code = self.code_text.get("1.0", "end-1c")
    language = self.language_entry.get()
    highlighted_code = apply_syntax_highlighting(code, language)
    self.code_text.delete("1.0", "end")
    self.code_text.insert("1.0", highlighted_code)


def highlight_custom_comments(code):
    """Highlight comments in the code."""
    highlighted_code = ""
    in_comment = False
    in_custom_context = False
    
    for line in code.splitlines():
        # Check for start of custom context
        if "<---" in line:
            in_custom_context = True
            start = line.index("<---")
            highlighted_code += line[:start]  # Text before the custom context
            highlighted_code += f"\033[92m{line[start:]}"  # Start highlighting
        elif "--->" in line and in_custom_context:
            end = line.index("--->") + 4  # Include the closing --->
            highlighted_code += f"{line[:end]}\033[0m"  # End highlighting
            highlighted_code += line[end:]  # Text after the custom context
            in_custom_context = False
        elif in_custom_context:
            highlighted_code += f"{line}\n"  # Inside custom context
        else:
            highlighted_code += f"{line}\n"  # Normal text

    return highlighted_code
