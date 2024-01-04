# language : en

Feature: Add a task to the to-do list
Scenario: Add a task to the to-do list

Given the to-do list is empty
When the user adds a task "comer"
Then the to-do list should contain "comer"

Feature: List all tasks in the to-do list.
Scenario: List all tasks in the to-do list
Given the to-do list contains tasks:
| comer |
| correr |
| hacer tarea |
When the user lists all tasks
Then the output should contain:
Tareas completadas:
[]
Tareas sin completar:
['comer', 'correr', 'hacer tarea']


Feature: Mark a task as completed.
Scenario: Mark a task as completed
Given the pending list contains tasks:
| comer |
| correr |
| hacer tarea |
When the user marks task "hacer tarea" as completed
Then the completed list should show task "hacer tarea"
Tareas completadas:
['hacer tarea']

Feature: Clear the entire to-do list.
Scenario: Clear the entire to-do list
Given the to-do list contains tasks:
| correr |
| comer |
| hacer tarea |
When the user clears the to-do list
Then the to-do list should be empty

Feature: Unmark a completed task
Scenario: Unmark a completed task
Given the completed list contains tasks:
| comer |
| correr |
When the user unmarks task "comer"
Then the completed list should not show task "comer"
Tareas completadas:
['correr']

Feature: Get total of tasks
Scenario: Get total of tasks
Given the completed list contains tasks:
| comer |
| correr |
When the user get the total of tasks
Then the output should contain:
Hay un total de: 2