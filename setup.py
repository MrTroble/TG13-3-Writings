import os
import datetime
import subprocess

system = "\"C:/Users/MrTroble/AppData/Local/Programs/Microsoft VS Code/Code.exe\" \""

today = datetime.date.today()

i = 0
dirs = []
for dir in os.listdir("."):
    if not os.path.isdir(dir) or dir == ".git": continue
    print(str(i) + " " + dir)
    dirs.append(dir)
    i += 1

while True:
    x = input("Subject: ")
    try:
        id = int(x)
    except:
        continue
    break

dirname = dirs[id]
name = input("Name: ")
path = os.path.join(dirname, name + " " + str(today) + ".md")
with open(path, "w") as fp:
    fp.write("# " + name)

py = input("Create py (y/n): ")
if py == "y":
    path2 = os.path.join(dirname, name + " " + str(today) + ".py")
    subprocess.call(system + path2 + "\"")

subprocess.call(system + path + "\"")
