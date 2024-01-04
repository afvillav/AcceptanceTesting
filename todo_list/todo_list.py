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

def unmark_task(ntarea):
    for x in completed:
        if x == ntarea:
            todo_list.append(x)
            completed.remove(x)

def count_tasks():
    count = 0
    for x in todo_list:
        count += 1
    for y in completed:
        count += 1
    return count

flag=True
print("Bienvenido al sistema de lista de quehaceres")
size=0
while(flag):
    print("Que desea hacer?(Escoja el numero de la tarea a realizar)")
    print("1.Añadir una nueva tarea\n2.Ver todas las tareas en la lista\n3.Marcar una tarea como completada\n4.Limpiar la lista\n5.Desmarcar una tarea\n6.Numero total de tareas\n7.Salir")
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
        todo_list.clear()
        completed.clear()
    elif (entry=="5"):
        print("Estas son las tareas completadas:")
        print(completed)
        print("Escoja que tarea desee desmarcar:")
        x=input()
        unmark_task(x)
    elif (entry=="6"):
        x= count_tasks()
        print("Hay un total de: "+ str(x))
    elif(entry=="7"):
        flag=False
