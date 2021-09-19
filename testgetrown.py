f = open("zoomLinks.txt", "r",encoding="utf-8")
strings = []
for string in f:
    strings.append(string)
f.close()
n = len(strings[:])
[print(i+1,":",strings[i].split(";")[0]) for i in range(n)]
print(n)

text = input('Skriv siffra för vilken länk du vill följa:')
row = int(text)-1
if row<0 or row>=n:
    print('Invalid number')
    exit()
info = (strings[row].split()[0]).split(";")
print(info)