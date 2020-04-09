
import base64

str="this is string"
str1=base64.b64encode('base64','strict')
print("Encoded string", str1)
print("Decoded string", base64.b64decode('base64','strict'))


