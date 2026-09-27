# Atividade AI1 - Tokens de identificadores e palavras reservadas

## O que foi resolvido

A solução foi implementada no lexer para reconhecer:

- identificadores do tipo `ID`
- palavras reservadas contidas em `Consts.KEYS`, retornando `KEY`
- números inteiros (`INT`) e reais (`FLOAT`)
- strings (`STRING`)
- símbolos básicos da linguagem (`+`, `-`, `*`, `/`, `=`, `(`, `)`, `[`, `]`, `,`)
- fim de arquivo (`$EOF`)

Os pontos principais da correção estão em:

- [Lexer.py](Lexer.py)
- [Token.py](Token.py)
- [Consts.py](Consts.py)

## Como validar no terminal

### 1) Entrar na pasta do projeto

```bash
cd "/home/thiago/Downloads/Individual - Compiladores"
```

### 2) Executar a validação direta do lexer

```bash
python3 - <<'PY'
from Lexer import Lexer

cases = [
    'let idade = 10',
    'if x1 > 1',
    'while contador == 2',
    'nome = "João"',
    'end',
    'x_1 + 3.14'
]

for text in cases:
    tokens, error = Lexer(text).makeTokens()
    print('INPUT:', text)
    print('TOKENS:', tokens)
    print('ERROR:', error)
    print('---')
PY
```

Saída esperada de exemplo:

```text
INPUT: let idade = 10
TOKENS: [KEY:let, ID:idade, =:=, INT:10, $EOF]
ERROR: None
```

### 3) Executar o REPL interativo

```bash
python3 main.py
```

No prompt, teste entradas como:

```text
let idade = 10
nome = "João"
while contador == 2
x_1 + 3.14
```

Para sair do REPL:

```text
:q
```

## Observações

- A palavra reservada `let` retorna `KEY:let`.
- Identificadores como `idade`, `x1`, `contador` e `x_1` retornam `ID`.
- Se a palavra estiver na lista `Consts.KEYS`, ela é classificada como palavra-chave e não como identificador comum.
- A validação foi executada com sucesso no ambiente local com o comando acima.
