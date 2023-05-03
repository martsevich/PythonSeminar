# определить палиндром или нет

txt = input("enter txt: ")
def polindrom_check(txt):
    if len(txt) < 2:
        return True
    if txt[0] != txt[-1]:
        return False
    return polindrom_check(txt[1:-1])
print(polindrom_check(txt))