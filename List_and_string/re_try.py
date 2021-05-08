string = 'hello this is 67678'

import re
str = re.findall(r"\d",string)
print(str)
str = set(re.findall(r"\d",string))
print(str)
str = re.findall(r"\d{2}",string)
print(str)
