crypt = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
        bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
        sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
        """
     
arr1 = crypt.split()
decrypt = "" 
   
for word in arr1:
    wordList = list(word)
    print(wordList)
    index = 0
    for letter in wordList:
        a = ord(letter)
        if a == 121 or a == 122:
            a = a - 26
        if a == 46:
            decrypt = decrypt + '.'
        elif a == 40 or a == 41 or a == 39:
            decrypt += chr(a)
            pass
        else:
            letter = chr(a + 2)
            print(letter)
            decrypt = decrypt + letter
            index = index +1
    decrypt = decrypt + ' '
print(decrypt)