def dari(command):
    s = command.replace("()", "o")
    s = s.replace("(", "")
    s = s.replace(")","")
    return s
g = str(input())
j = dari(g)
print(j)