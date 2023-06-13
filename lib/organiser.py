import re

class Organiser:
    def __init__(self):
        self.all_entries = []
        self.all_contacts = []
        self.all_todo_tasks = []

    def all_diary_entries(self):
        return sorted(self.all_entries, key = lambda x: x.date_added, reverse=True)

    def add_diary_entry(self, entry):
        self.all_entries.append(entry)
    
    def reading_time(self, wpm, minutes):
        total_words = wpm * minutes
        reading_dictionary = {}
        for entry in self.all_entries:
            if entry.word_count() < total_words:
                reading_dictionary[entry] = entry.word_count()
        max = 0
        for item, val in reading_dictionary.items():
            if val > max:
                max = val
                best_val = item
        return best_val
    
    def return_contacts(self):
        for entry in self.all_diary_entries():
            PhoneNumber = re.search(r'\b\d{11}\b', entry.contents) 
            if PhoneNumber:
                self.all_contacts.append(PhoneNumber.group()) # .group() extracts string from re.PhoneNumber object
        return self.all_contacts
    
    def add_todo_task(self, task):
        self.all_todo_tasks.append(task)

    def all_tasks(self):
        return [task.task_todo for task in self.all_todo_tasks]



class DiaryEntry:
    def __init__(self, title, contents, date_added):
        self.title = title
        self.contents = contents
        self.date_added = date_added
    
    def word_count(self):
        split_str = self.contents.split()
        return len(split_str)
    
        
class TodoTask:
    def __init__(self, task_todo):
        self.task_todo = task_todo


