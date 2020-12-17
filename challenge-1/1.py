in_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
in_str = "liwqih"
out_str = ""

for char in in_str:
    if char == ' ':
        out_str += ' '
    else:
        ord_num = ord(char)


        if ord('a') <= ord_num <= ord('z'):
            ord_cyp = ord_num - 2

            if ord_cyp%ord('z') < ord('a'):
                out_str += chr(ord_cyp%ord('z') + ord('a') -1)
            else:
                out_str += chr(ord_cyp)
        else:
            out_str += chr(ord(char))


# print(String.maketrans('map'))
print(out_str)