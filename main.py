file = open("text.txt", "r")
s = file.read()
k = 0
for i in s:
    k += 1
print(f"Количество символов в файле: {k}")