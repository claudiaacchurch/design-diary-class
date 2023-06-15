from lib.organiser import TodoTask, TaskList

#integration TaskList and TodoTask

#1 TaskList.all_tasks returns list of all todo items
def test_all_tasks_returns_list_of_tasks():
    task_list = TaskList()
    task1 = TodoTask("wash the floor")
    task2 = TodoTask("walk the dog")
    task_list.add_todo_task(task1)
    task_list.add_todo_task(task2)
    result = task_list.all_tasks()
    assert result == ["wash the floor", "walk the dog"]

#2 Organiser.completed returns list of task objects with is_complete == True
def test_completed_returns_completed_tasks():
    task_list = TaskList()
    task1 = TodoTask("wash the floor")
    task2 = TodoTask("walk the dog")
    task_list.add_todo_task(task1)
    task_list.add_todo_task(task2)
    task1.mark_complete()
    result = task_list.all_completed()
    assert result == [task1]


#2 TodoTask.incomplete returns list of tasks where is_complete == False
def test_completed_returns_incomplete_tasks():
    task_list = TaskList()
    task1 = TodoTask("wash the floor")
    task2 = TodoTask("walk the dog")
    task_list.add_todo_task(task1)
    task_list.add_todo_task(task2)
    task1.mark_complete()
    result = task_list.all_incomplete()
    assert result == [task2]