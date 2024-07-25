key = input("Digite uma palavra e crie uma senha: ")

password = ""

for letter in key:
    if letter in "Aa": password = password + "95"
    elif letter in "Bb": password = password + "J"
    elif letter in "Cc": password = password + "1l"
    elif letter in "Çç": password = password + "%"
    elif letter in "Dd": password = password + "T"
    elif letter in "Ee": password = password + "#k"
    elif letter in "Ff": password = password + "@"
    elif letter in "Gg": password = password + "4"
    elif letter in "Hh": password = password + "Ax"
    elif letter in "Ii": password = password + "F"
    elif letter in "Jj": password = password + "7"
    elif letter in "Kk": password = password + "$"
    elif letter in "Ll": password = password + "@g"
    elif letter in "Mm": password = password + "#"
    elif letter in "Nn": password = password + "Rc"
    elif letter in "Oo": password = password + "B"
    elif letter in "Pp": password = password + "6"
    elif letter in "Qq": password = password + "u"
    elif letter in "Rr": password = password + "eZ"
    elif letter in "Ss": password = password + "38"
    elif letter in "Tt": password = password + "&"
    elif letter in "Uu": password = password + "m"
    elif letter in "Vv": password = password + "2"
    elif letter in "Ww": password = password + "i"
    elif letter in "Xx": password = password + "nS"
    elif letter in "Yy": password = password + "d"
    elif letter in "Zz": password = password + "0o"
    else: password = password + letter
    
print(password)