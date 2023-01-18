import os

s = 0
while True:
    joyi = input()
    if joyi != "exet":
        print(len(os.listdir(joyi)))
    else:
        break
    s = s + len(os.listdir(joyi))
print(s)
