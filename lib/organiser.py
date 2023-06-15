import re
from datetime import datetime, date

class Organiser:
    def __init__(self):
        self.all_entries = []
        self.all_contacts = []
        self.all_todo_tasks = []
        self.completed_tasks = []
        self.incomplete_tasks = []

    #DiaryEntry
    def all_diary_entries(self):
        return sorted(self.all_entries, key = lambda x: x.date_added, reverse=True)
    
    def add_diary_entry(self, entry):
        self.all_entries.append(entry)
    
    '''As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much
    time I have and my reading speed'''

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
    
    '''As a user
    So that I can reflect on my experiences
    I want to read my past diary entries'''

    def read(self, date_added):
        contents_to_read = []
        for entry in self.all_entries:
            if entry.date_added == date_added:
                contents_to_read.append(entry.contents)
    
        return contents_to_read

    
    '''As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile
    phone numbers in all my diary entries'''

    #Contacts from DiaryEntry
    def return_contacts(self):
        for entry in self.all_diary_entries():
            PhoneNumber = re.search(r'\b\d{11}\b', entry.contents) 
            if PhoneNumber:
                self.all_contacts.append(PhoneNumber.group()) # .group() extracts string from re.PhoneNumber object
        return self.all_contacts
    
    '''As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary'''

    #TodoTask
    def add_todo_task(self, task):
        self.all_todo_tasks.append(task)

    def all_tasks(self):
        return [task.task_todo for task in self.all_todo_tasks]
    
    def all_completed(self):
        for task in self.all_todo_tasks:
            if task.is_complete == True:
                self.completed_tasks.append(task)
        return self.completed_tasks
        
    def all_incomplete(self):
        for task in self.all_todo_tasks:
            if task.is_complete == False:
                self.completed_tasks.append(task)
        return self.completed_tasks



class DiaryEntry:

    '''As a user
    So that I can record my experiences
    I want to keep a regular diary'''

    def __init__(self, title, contents, date_added):
        if not isinstance(title, str) or not isinstance(contents, str):
            raise Exception("Arguments must be of type str")
        elif not isinstance(date_added, date):
            raise Exception("Argument must be of type date")
        self.title = title
        self.contents = contents
        self.date_added = date_added
    
    def word_count(self):
        split_str = self.contents.split()
        return len(split_str)
        
class TodoTask:
    def __init__(self, task_todo):
        self.task_todo = task_todo
        self.is_complete = False

    def mark_complete(self):
        self.is_complete = True 


