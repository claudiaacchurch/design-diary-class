from lib.organiser import TodoTask
import pytest

# Unit tests for TodoTask

#1 TodoTask.mark_complete() changes is_complete to True
def test_todo_mark_complete_changes_is_complete():
    task = TodoTask("wash the floor")
    task.mark_complete()
    assert task.is_complete == True

#2 Raise error if TodoTask is not str
def test_raises_error_if_task_not_str():
    with pytest.raises(Exception) as e:
        TodoTask(9879)
    assert str(e.value) == "TypeError"