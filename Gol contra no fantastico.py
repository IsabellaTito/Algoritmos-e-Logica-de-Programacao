info = input().strip()
info1 = info[::-1]
nome = info1[0:len(info1)-3].title().strip()
info = info.split()
if info[0] == "c":
    if info[1] == "0":
        print(nome)
    else:
        print(nome+nome[-1]*4)
else:
    if info[1] == "0":
        print(str(*info[2::]))
    else:
        print(str(*info[2::])+info[-1][-1]*4)
