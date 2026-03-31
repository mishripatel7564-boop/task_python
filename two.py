"""src=open("new.txt","r")
data=src.read()
src.close()

dst=open("old.txt","w")
dst.write(data)
dst.close()
print("file copied successfully")"""
with open("new.txt","r")as f1,open("old.txt","r")as f2,open("create.txt","w")as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())
    print("files mearged successfully")