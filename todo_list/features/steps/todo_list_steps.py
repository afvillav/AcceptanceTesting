from behave import given, when, then, And
#Scenario: Add a task to the to-do list

#Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
# Set the to-do list as an empty list
    global todo_list
    todo_list = []

#Step 2: When the user adds a task "comer"
@when('the user adds a task "{task}"')
def step_impl(context, task):
# Add the task to the to-do list
    global todo_list
    todo_list.append(task)

#Step 3: Then the to-do list should contain "comer"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
# Check if the task is in the to-do list
    assert task in todo_list, f'Task "{task}" not found in the to-do list'



#Scenario: List all tasks in the to-do list

#Step 1: Given the todo_list contains tasks:
@given('the to-do list should contain "comer","correr,"hacer tarea"')
def step_impl(context):
# Set the to-do list as with data
    global todo_list
    todo_list = []
    todo_list.append("comer")
    todo_list.append("correr")
    todo_list.append("hacer tarea")

#Step 2: When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
# The user lists all tasks
    global todo_list
    print(todo_list)

#Step 3: Then the to-do list should contain "comer", "correr", "hacer tarea"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
# Check if the tasks are in the to-do list
    lista = ["correr","comer","hacer tarea"]
    for x in lista:
        assert x in todo_list, f'Task "{x}" not found in the to-do list'



#Scenario: Mark a task as completed

#Step 1: Given the todo_list list contains tasks:
@given('the to-do list should contain "comer","correr,"hacer tarea"')
def step_impl(context):
# Set the to-do list as with data
    global todo_list
    todo_list = []
    todo_list.append("comer")
    todo_list.append("correr")
    todo_list.append("hacer tarea")

#Step 2: When the user marks task "hacer tarea" as completed
@when('the user adds a task to completed list"{task}"')
def step_impl(context, task):
# Add the task to the to-do list
    global completed
    completed.append(task)

#Step 3: Then the completed list should contain "comer"
@then('the completed list should contain "{task}"')
def step_impl(context, task):
# Check if the task is in the completed list
    assert task in completed, f'Task "{task}" not found in the to-do list'

#Step 4: Then the todo_list list should not contain "comer"
@And('the todo_list should not contain "{task}"')
def step_impl(context, task):
# Check if the task is not in the todo_list
    assert task in todo_list, f'Task "{task}" should not be in the to-do list'


#Scenario: Clear the entire to-do list
#Step 1: Given the todo_list list contains tasks:
@given('the to-do list should contain "comer","correr"')
def step_impl(context):
# Set the to-do list as with data
    global todo_list
    todo_list = []
    todo_list.append("comer")
    todo_list.append("correr")

#Step 2: When the user clears the to-do list
@when('the user clears the todo_list')
def step_impl(context):
# clear the todo_list
    global todo_list
    todo_list.clear()
#Step 3: Then the to-do list should be empty
@then('the completed list should be empty')
def step_impl(context):
# check the todo_list is empty
    global todo_list
    assert not todo_list, 'The to-do list is not empty'

#Scenario: Unmark a completed task
#Step 1: Given the todo_list list contains tasks:
@given('the to-do list should contain "comer","correr,"hacer tarea"')
def step_impl(context):
# Set the to-do list as with data
    global todo_list
    todo_list = []
    todo_list.append("comer")
    todo_list.append("correr")

#Step 2: When the user unmarks task "comer"
@when('the user adds a task to completed list"{task}"')
def step_impl(context, task):
# Add the task to the to-do list
    global completed
    todo_list.append(task)

#Step 3: Then the todo_list list should contain "comer"
@then('the completed list should contain "{task}"')
def step_impl(context, task):
# Check if the task is in the completed list
    assert task in todo_list, f'Task "{task}" not found in the to-do list'

#Step 4: Then the completed list should not contain "comer"
@And('the todo_list should not contain "{task}"')
def step_impl(context, task):
# Check if the task is not in the todo_list
    assert task in completed, f'Task "{task}" should not be in the to-do list'
    

#Scenario: Get total of tasks
#Step 1: Given the todo_list list contains tasks:
@given('the to-do list should contain "comer","correr,"hacer tarea"')
def step_impl(context):
# Set the to-do list as with data
    global todo_list
    todo_list = []
    todo_list.append("comer")
    todo_list.append("correr")

#Step 2: When the gets the total number of tasks
@when('the user adds a task "{task}"')
def step_impl(context, task):
# count the number of tasks
    global count_tasks
    x=count_tasks()

#Step 3: Then the output should contain "Hay un total de: 2"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
# Check if the total is correct
    assert x == 2, f'Expected total: {2}, Actual: {x}'