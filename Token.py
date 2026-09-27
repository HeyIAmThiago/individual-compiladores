class Token:
  def __init__(self, _type, _value=None) -> None:
    self.type = _type
    self.value = _value

  def matches(self, _type, _value):
    return self.type == _type and self.value == _value

  def __repr__(self):
    if self.value is not None:
      return f'{self.type}:{self.value}'
    return f'{self.type}'
