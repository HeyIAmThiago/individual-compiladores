from Token import Token
from Consts import Consts
from Error import Error

class Lexer:
  def __init__(self, source_code) -> None:
    self.code = source_code
    self.current = None
    self.indice, self.coluna, self.linha = -1, -1, 0
    self.__advance()

  def __advance(self):
    self.__advanceCalc()
    self.current = self.code[self.indice] if self.indice < len(self.code) else None

  def __advanceCalc(self):
    self.indice += 1
    self.coluna += 1
    if self.current == '\n':
      self.linha += 1
      self.coluna = 0
    return self

  def makeTokens(self):
    tokens = []
    while self.current != None:
      if self.current in ' \t\r\n':
        self.__advance()
      elif self.current == Consts.PLUS:
        tokens.append(Token(Consts.PLUS, Consts.PLUS))
        self.__advance()
      elif self.current == Consts.MINUS:
        tokens.append(Token(Consts.MINUS, Consts.MINUS))
        self.__advance()
      elif self.current == Consts.MUL:
        tokens.append(Token(Consts.MUL, Consts.MUL))
        self.__advance()
      elif self.current == Consts.DIV:
        tokens.append(Token(Consts.DIV, Consts.DIV))
        self.__advance()
      elif self.current == Consts.EQ:
        tokens.append(Token(Consts.EQ, Consts.EQ))
        self.__advance()
      elif self.current == Consts.LPAR:
        tokens.append(Token(Consts.LPAR, Consts.LPAR))
        self.__advance()
      elif self.current == Consts.RPAR:
        tokens.append(Token(Consts.RPAR, Consts.RPAR))
        self.__advance()
      elif self.current == Consts.LSQUARE:
        tokens.append(Token(Consts.LSQUARE, Consts.LSQUARE))
        self.__advance()
      elif self.current == Consts.RSQUARE:
        tokens.append(Token(Consts.RSQUARE, Consts.RSQUARE))
        self.__advance()
      elif self.current == Consts.COMMA:
        tokens.append(Token(Consts.COMMA, Consts.COMMA))
        self.__advance()
      elif self.current in Consts.DIGITOS:
        tokens.append(self.__makeNumber())
        continue
      elif self.current == '"':
        string = self.__MakeString()
        if self.current != '"':
          return [], Error(f"{Error.lexerError}: expecting '\"', {self.current} was served")
        self.__advance()
        tokens.append(string)
      elif self.current.isalpha() or self.current == Consts.UNDER:
        tokens.append(self.__makeIdentifier())
        continue
      else:
        return tokens, Error(f"{Error.lexerError}: unexpected character '{self.current}'")

    tokens.append(Token(Consts.EOF))
    return tokens, None

  def __makeNumber(self):
    strNum = ''
    conta_ponto = 0
    while self.current != None and self.current in Consts.DIGITOS + '.':
      if self.current == '.':
        if conta_ponto == 1: break
        conta_ponto += 1
      strNum += self.current
      self.__advance()

    if conta_ponto == 0:
      return Token(Consts.INT, int(strNum))
    return Token(Consts.FLOAT, float(strNum))

  def __makeIdentifier(self):
    value = ''
    while self.current != None and (self.current.isalnum() or self.current == Consts.UNDER):
      value += self.current
      self.__advance()

    if value in Consts.KEYS:
      return Token(Consts.KEY, value)
    return Token(Consts.ID, value)

  def __MakeString(self):
      stri = ""
      bypass = False
      self.__advance()
      specialChars = {'n':'\n', 't': '\t'}
      while (self.current != None and (self.current != '"' or bypass)):
          if (bypass):
              c = specialChars.get(self.current, self.current)
              stri += c
              bypass = False
          else:
              if (self.current == '\\'):
                  bypass = True
              else:
                  stri += self.current
          self.__advance()
      return Token(Consts.STRING, stri)
