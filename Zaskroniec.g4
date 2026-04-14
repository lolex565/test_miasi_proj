grammar Zaskroniec;

program : element* EOF ;

element
    // Control Flow
    : IF | ELIF | ELSE | WHILE | FOR | IN | BREAK | CONTINUE | PASS | DO
    // Functions & Classes
    | DEF | RETURN | CLASS | YIELD | LAMBDA | APPLY | TO
    // Logical & Identity
    | AND | OR | NOT | IS
    // Booleans & None
    | TRUE | FALSE | NONE
    // Context & Modules
    | WITH | IMPORT | FROM | AS
    // Exceptions & Assertions
    | TRY | EXCEPT | FINALLY | RAISE | ASSERT
    // Scope & Async & Memory
    | GLOBAL | NONLOCAL | ASYNC | AWAIT | DEL
    // Builtin functions & types
    | PRINT | RANGE | LEN | STR | INT | FLOAT | BOOL | LIST | DICT | SET | TUPLE
    | ABS | SUM | MIN | MAX | ROUND | TYPE | OPEN
    // Generic tokens
    | ID | STRING | NUMBER | WS | SYMBOL
    ;

// ==========================================
// 1. Control Flow (Przepływ sterowania)
// ==========================================
IF : 'jezeli' | 'jesli';
ELIF : 'albo_jesli';
ELSE : 'inaczej' | 'w_przeciwnym_razie';
WHILE : 'dopoki';
FOR : 'dla';
IN : 'w';
BREAK : 'przerwij';
CONTINUE : 'kontynuuj';
PASS : 'pomin';
DO : 'wykonuj';

// ==========================================
// 2. Functions & Classes (Funkcje i klasy)
// ==========================================
DEF : 'zdefiniuj';
RETURN : 'zwroc';
CLASS : 'klasa';
YIELD : 'dostarcz';
LAMBDA : 'anonimowa';
APPLY : 'zastosuj';
TO : 'do';

// ==========================================
// 3. Logical Operators & Identity (Operatory)
// ==========================================
AND : 'oraz';
OR : 'lub' | 'albo';
NOT : 'nie';
IS : 'jest';

// ==========================================
// 4. Booleans & None (Wartości logiczne i Nic)
// ==========================================
TRUE : 'Prawda';
FALSE : 'Falsz';
NONE : 'Nic';

// ==========================================
// 5. Imports & Context (Importy i konteksty)
// ==========================================
IMPORT : 'zaimportuj';
FROM : 'z';
AS : 'jako';
WITH : 'z_kontekstem';

// ==========================================
// 6. Exceptions & Assert (Wyjątki i asercje)
// ==========================================
TRY : 'sprobuj';
EXCEPT : 'przechwyc' | 'wyjatek';
FINALLY : 'wreszcie';
RAISE : 'rzuc';
ASSERT : 'zapewnij';

// ==========================================
// 7. Scope, Async, Memory (Zasięg, Asynchroniczność, Pamięć)
// ==========================================
GLOBAL : 'globalna';
NONLOCAL : 'nielokalna';
ASYNC : 'asynchronicznie';
AWAIT : 'oczekuj';
DEL : 'usun';

// ==========================================
// 8. Built-in Functions & Types (Wbudowane)
// ==========================================
PRINT : 'wypisz';
RANGE : 'zasieg';
LEN : 'dlugosc';
STR : 'napis';
INT : 'calkowita';
FLOAT : 'zmienna_przecinkowa';
BOOL : 'logiczna';
LIST : 'lista';
DICT : 'slownik';
SET : 'zbior';
TUPLE : 'krotka';
ABS : 'bezwzgledna';
SUM : 'suma';
MIN : 'minimum';
MAX : 'maksimum';
ROUND : 'zaokraglij';
TYPE : 'typ';
OPEN : 'otworz';

// ==========================================
// 9. Fundamental Tokens (Podstawowe)
// ==========================================
ID : [a-zA-Z_][a-zA-Z0-9_]*;
STRING : '"""' .*? '"""' | '\'\'\'' .*? '\'\'\'' | '"' ~["]* '"' | '\'' ~[']* '\'' ;
NUMBER : [0-9]+ ('.' [0-9]+)?;
WS : [ \t\r\n\f]+;
SYMBOL : .;
