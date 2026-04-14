import sys
import os
import subprocess
import re
from antlr4 import *
from ZaskroniecLexer import ZaskroniecLexer

def transform_extended_constructs(code):
    lines = code.splitlines(keepends=True)
    transformed = []
    do_stack = []

    let_pattern = re.compile(r'^(\s*)let\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+?)\s*(#.*)?$')
    do_pattern = re.compile(r'^(\s*)do\s*:\s*(#.*)?$')
    while_pattern = re.compile(r'^(\s*)while\s+(.+?)\s*(#.*)?$')

    for line in lines:
        stripped_line = line.rstrip('\r\n')
        newline = line[len(stripped_line):]

        let_match = let_pattern.match(stripped_line)
        if let_match:
            indent, variable_name, expression, comment = let_match.groups()
            new_line = f"{indent}{variable_name} = {expression}"
            if comment:
                new_line += f" {comment}"
            transformed.append(new_line + newline)
            continue

        do_match = do_pattern.match(stripped_line)
        if do_match:
            indent = do_match.group(1)
            do_stack.append(indent)
            transformed.append(f"{indent}while True:{newline}")
            continue

        while_match = while_pattern.match(stripped_line)
        if while_match and do_stack:
            indent, condition, comment = while_match.groups()
            if indent == do_stack[-1]:
                do_stack.pop()
                inner_indent = f"{indent}    "
                transformed.append(f"{inner_indent}if not ({condition}):{newline}")
                transformed.append(f"{inner_indent}    break{newline}")
                if comment:
                    transformed[-2] = transformed[-2].rstrip('\r\n') + f" {comment}" + newline
                continue

        transformed.append(line)

    return "".join(transformed)

def main():
    if len(sys.argv) < 2:
        print("Uzycie: python zaskroniec.py <plik.zas>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Blad: Plik {input_file} nie istnieje.")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()

    input_stream = InputStream(code)
    lexer = ZaskroniecLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    # Tabela zamiany z tokenów ANTLR Zaskrońca na tokeny Pythona
    token_map = {
        ZaskroniecLexer.PRINT: "print",
        ZaskroniecLexer.WHILE: "while",
        ZaskroniecLexer.DO: "do",
        ZaskroniecLexer.IF: "if",
        ZaskroniecLexer.ELIF: "elif",
        ZaskroniecLexer.ELSE: "else",
        ZaskroniecLexer.FOR: "for",
        ZaskroniecLexer.IN: "in",
        ZaskroniecLexer.DEF: "def",
        ZaskroniecLexer.RETURN: "return",
        ZaskroniecLexer.CLASS: "class",
        ZaskroniecLexer.YIELD: "yield",
        ZaskroniecLexer.LAMBDA: "lambda",
        ZaskroniecLexer.LET: "let",
        ZaskroniecLexer.TRUE: "True",
        ZaskroniecLexer.FALSE: "False",
        ZaskroniecLexer.NONE: "None",
        ZaskroniecLexer.AND: "and",
        ZaskroniecLexer.OR: "or",
        ZaskroniecLexer.NOT: "not",
        ZaskroniecLexer.IS: "is",
        ZaskroniecLexer.TRY: "try",
        ZaskroniecLexer.EXCEPT: "except",
        ZaskroniecLexer.FINALLY: "finally",
        ZaskroniecLexer.RAISE: "raise",
        ZaskroniecLexer.ASSERT: "assert",
        ZaskroniecLexer.PASS: "pass",
        ZaskroniecLexer.BREAK: "break",
        ZaskroniecLexer.CONTINUE: "continue",
        ZaskroniecLexer.IMPORT: "import",
        ZaskroniecLexer.FROM: "from",
        ZaskroniecLexer.AS: "as",
        ZaskroniecLexer.WITH: "with",
        ZaskroniecLexer.GLOBAL: "global",
        ZaskroniecLexer.NONLOCAL: "nonlocal",
        ZaskroniecLexer.ASYNC: "async",
        ZaskroniecLexer.AWAIT: "await",
        ZaskroniecLexer.DEL: "del",
        ZaskroniecLexer.RANGE: "range",
        ZaskroniecLexer.LEN: "len",
        ZaskroniecLexer.STR: "str",
        ZaskroniecLexer.INT: "int",
        ZaskroniecLexer.FLOAT: "float",
        ZaskroniecLexer.BOOL: "bool",
        ZaskroniecLexer.LIST: "list",
        ZaskroniecLexer.DICT: "dict",
        ZaskroniecLexer.SET: "set",
        ZaskroniecLexer.TUPLE: "tuple",
        ZaskroniecLexer.ABS: "abs",
        ZaskroniecLexer.SUM: "sum",
        ZaskroniecLexer.MIN: "min",
        ZaskroniecLexer.MAX: "max",
        ZaskroniecLexer.ROUND: "round",
        ZaskroniecLexer.TYPE: "type",
        ZaskroniecLexer.OPEN: "open"
    }

    output_code = []
    
    for token in stream.tokens:
        if token.type == Token.EOF:
            break
        if token.type in token_map:
            output_code.append(token_map[token.type])
        else:
            output_code.append(token.text)
            
    compiled_code = "".join(output_code)
    compiled_code = transform_extended_constructs(compiled_code)
    out_filename = input_file + ".py"
    
    with open(out_filename, 'w', encoding='utf-8') as f:
        f.write(compiled_code)
        
    print(f"[Zaskroniec] Zakończono translację kodowania pliku. Wykonywane... ({out_filename})\n")
    print("-" * 50)
    # Wykonanie utworzonego pliku Pythona
    subprocess.run([sys.executable, out_filename])
    print("-" * 50)
    print("\n[Zaskroniec] Program zakończony pomyślnie.")

if __name__ == '__main__':
    main()
