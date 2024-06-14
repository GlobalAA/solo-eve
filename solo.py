import json


class Solo:
  def __init__(self, string: str) -> None:
    self.data = string
    self.lang_dict = json.load(open('language.json', 'rb'))

  @staticmethod
  def version():
    return 'Solo-32'

  def encode_eve(self):
    for key, value in self.lang_dict.items():
      self.data = self.data.replace(key, str(value))
    return self.data

  def decode_eve(self):
    for key, value in self.lang_dict.items():
      self.data = self.data.replace(str(value), key)
    return self.data