from lib.organiser import Organiser, TodoTask

#integration Organiser and TodoTask

#1 Organiser.all_tasks returns list of all todo items
def test_all_tasks_returns_list_of_tasks():
    organiser = Organiser()
    task1 = TodoTask("wash the floor")
    task2 = TodoTask("walk the dog")
    organiser.add_todo_task(task1)
    organiser.add_todo_task(task2)
    result = organiser.all_tasks()
    assert result == ["wash the floor", "walk the dog"]

