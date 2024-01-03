todo_list=[]
completed=[]

def add_todo(task):
    global size
    todo_list.append(task)
    size +=1

def mark_task(ntarea):
    for x in todo_list:
        if x == ntarea:
            completed.append(x)
        todo_list.remove(x)

flag=True
print("Bienvenido al sistema de lista de quehaceres")
size=0
while(flag):
    print("Que desea hacer?(Escoja el numero de la tarea a realizar)")
    print("1.Añadir una nueva tarea\n2.Ver todas las tareas en la lista\n3.Marcar una tarea como completada\n4.Limpiar la lista\n5.Salir")
    entry= input()
    if (entry=="1"):
        print("Ingrese la tarea que desea añadir")
        tarea=input()
        add_todo(tarea)
    elif (entry=="2"):
        print("Tareas completadas:")
        print(completed)
        print("Tareas sin completar:")
        print(todo_list)
    elif(entry=="3"):
        print("Estas son las tareas sin completar:")
        print(todo_list)
        print("Escoja que tarea desea marcar como completada")
        x=input()
        mark_task(x)
    elif (entry=="4"):
        todo_list.clear
        completed.clear
    elif(entry=="5"):
        flag=False
