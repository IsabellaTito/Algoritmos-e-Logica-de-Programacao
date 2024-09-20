pala = input().split(",")
verbo = []
for i in range(len(pala)):
    terR = pala[i].endswith("r")
    terU = pala[i].endswith("ur")
    if terR == True and terU == False:
        verbo.append(pala[i].strip())
if len(verbo) == 0:
    print("temos 0 palavra(s) no infitivo.")
else:
    print("temos",len(verbo),"palavra(s) no infitivo.")
    for i in range(len(verbo)):
        if verbo[i].endswith("ar"):
            gerun = verbo[i][-len(verbo[i]):-1:1] + "ndo"
            print("o verbo", verbo[i], "no Gerúndio é:", gerun)
            parti = verbo[i][-len(verbo[i]):-1:1] + "do"
            print("o verbo", verbo[i], "no Particípio é:", parti)
            vt = verbo[i][-2]
            print("a vogal temática do verbo",verbo[i],"é", vt)
            rad = verbo[i][-len(verbo[i]):-2:1]
            print("o radical do verbo", verbo[i], "é", rad)
            print("O verbo", verbo[i], "é da primeira conjugação.")
            print()
        elif verbo[i].endswith("er"):
            gerun = verbo[i][-len(verbo[i]):-1:1] + "ndo"
            print("o verbo", verbo[i], "no Gerúndio é:", gerun)
            parti = verbo[i][-len(verbo[i]):-2:1] + "ido"
            print("o verbo", verbo[i], "no Particípio é:", parti)
            vt = verbo[i][-2]
            print("a vogal temática do verbo",verbo[i],"é", vt)
            rad = verbo[i][-len(verbo[i]):-2:1]
            print("o radical do verbo", verbo[i], "é", rad)
            print("O verbo", verbo[i], "é da segunda conjugação.")
            print()
        elif verbo[i].endswith("ir"):
            gerun = verbo[i][-len(verbo[i]):-1:1] + "ndo"
            print("o verbo", verbo[i], "no Gerúndio é:", gerun)
            parti = verbo[i][-len(verbo[i]):-1:1] + "do"
            print("o verbo", verbo[i], "no Particípio é:", parti)
            vt = verbo[i][-2]
            print("a vogal temática do verbo",verbo[i],"é", vt)
            rad = verbo[i][-len(verbo[i]):-2:1]
            print("o radical do verbo", verbo[i], "é", rad)
            print("O verbo", verbo[i], "é da terceira conjugação.")
            print()
        elif verbo[i].endswith("or"):
            gerun = verbo[i][-len(verbo[i]):-1:1] + "ndo"
            print("o verbo", verbo[i], "no Gerúndio é:", gerun)
            parti = verbo[i][-len(verbo[i]):-1:1] + "sto"
            print("o verbo", verbo[i], "no Particípio é:", parti)
            vt = verbo[i][-2]
            print("a vogal temática do verbo",verbo[i],"é", vt)
            rad = verbo[i][-len(verbo[i]):-2:1]
            print("o radical do verbo", verbo[i], "é", rad)
            print("O verbo", verbo[i], "é da segunda conjugação.")
            print()
