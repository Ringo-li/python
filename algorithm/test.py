import re

print(re.sub('\B(?=(\d{3})+(?!\d))',',','1234567890'))
# "1234567890".replace(\B(?=(?:\d{3})+(?!\d)),",") 

print(re.sub('中国.*?(\w{3}).*?中国(?=人)','brave \1 china','中国 love 中国人'))