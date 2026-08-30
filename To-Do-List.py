tasks = input("Einter your To Do list tasks...")
PrepareTasks = tasks.split(",")
print('')
ToDo =[]
ToDo.extend(PrepareTasks)
print(ToDo)
print("")
modulationChoose=-1
ask= input("Do you want modulation?..\nYse.\nNo \n")
if ask =="Yse":
   modulation = input("if you want to modulation choose...\n1 add task. \n2 delet task. \n3 switch task \n4 delet all ")
   modulationChoose = int(modulation)
else:
   modulation=""
   print(ToDo)

print("")

if modulationChoose==1:
   tasks = input("Einter your To Do list tasks...")
   PrepareTasks = tasks.split(",")
   ToDo.extend(PrepareTasks)
   print(ToDo)

elif modulationChoose==2:
 print(ToDo)
 delet= input ("choose what you want to delet...")
 ToDo.remove(delet)
 print(ToDo)
elif modulationChoose==3:
   print(ToDo)
   switch=input("choose what you want to switch with...")
   tasks = input("Einter your To Do list tasks...")
   PrepareTasks = tasks.split(",")
   position = ToDo.index(switch)
   ToDo[position] =tasks
   print(ToDo)
elif modulationChoose==4:
   ToDo.clear()
   print(ToDo)
else:
   print(ToDo)
 
