import re
strings = '''Visual Studio Code is a lightweight but powerful source code 
and vis editor which runs on your desktop and is available for Windows, macOS and Linux. phone number is 7032043837 It comes with built-in support for JavaScript, TypeScript and Node.js'''
pattern = '\d{10}'
matches = re.findall(pattern,strings)
print(matches)

num = "139ed9h02398ounds:fjwnduw:wdicdw+jd-jb     iuhedhwfek:vsdycbj wnuc"
pat = '[^:]+'
a = re.findall(pat,num)
print(a)