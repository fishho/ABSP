#! python3
# regexStrip-- regex version string strip()

import re, sys
def regexStrip(string, bad=' '):
    stripReg = re.compile('[%s]' % bad)
    return stripReg.sub('', string)
string = input("请输入字符串")
bad= input("请输入要替换的")
print(regexStrip(string,bad))