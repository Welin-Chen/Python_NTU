intab = "013457"
outtab = "OIEAST"
trantab = str.maketrans(intab, outtab)
str_intput = input()
str_output = str_intput.translate(trantab)
print(str_output)
