import pyclip
try:
    pyclip.paste().decode("utf-8")
except:
    cliptype = "bin"
else:
    cliptype = "txt"
print(cliptype)