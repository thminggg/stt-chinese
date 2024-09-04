import opencc
import pyperclip

converter = opencc.OpenCC('s2t.json')
converted = converter.convert("""""")
print(converted)
pyperclip.copy(converted)

