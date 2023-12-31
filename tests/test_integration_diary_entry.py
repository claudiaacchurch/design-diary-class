from lib.organiser import Diary, DiaryEntry
from datetime import datetime, timedelta

current_date = datetime.now()
current_date = current_date.date() #remove time
formatted_date = current_date.strftime('%d%m%Y') #format -> str
new_date = datetime.strptime(formatted_date, '%d%m%Y') #strptime -> datetime
two_days_ago = new_date - timedelta(days = 2)

#integration Diary and DiaryEntry

#1 Diary.all_diary_entries returns list of diary entry objects ordered by date added in descending order.
def test_diary_entries_returns_list_ordered_by_date():
    diary = Diary()
    entry1 = DiaryEntry("Entry1", "This is my first diary entry", two_days_ago)
    entry2 = DiaryEntry("Entry2", "This is today's entry", new_date)
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    result = diary.all_diary_entries()
    assert result == [entry2, entry1]

#2 Diary.reading_time returns best diary entry to read for the given time and speed.
def test_reading_time_returns_best_diary_entry():
    diary = Diary()
    entry1 = DiaryEntry("Entry1", "This is my first diary entry, this is a much longer one I will keep going blah blah blah", two_days_ago)
    entry2 = DiaryEntry("Entry2", "This is today's entry", new_date)
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    result = diary.reading_time(10, 2)
    assert result == entry1

#3 Diary.return_contacts returns list of mobile phone numbers from all diary entries sorted by date_added in decending order.
def test_return_contacts_returns_list_of_diary_phone_numbers():
    diary = Diary()
    entry1 = DiaryEntry("Entry1", "This is my first diary entry, today I met my friend Lucy her number is 08987654321", two_days_ago)
    entry2 = DiaryEntry("Entry2", "This is another entry", two_days_ago)
    entry3 = DiaryEntry("Entry2", "This is today's entry, today I met Tom: 09856789034", new_date)
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_diary_entry(entry3)
    result = diary.return_contacts()
    assert result == ['09856789034', '08987654321']

#4 Diary.read() returns contents of entry filtered on date (one entry)
def test_read_returns_diary_contents():
    diary = Diary()
    entry1 = DiaryEntry("Entry1", "This is today's entry", new_date)
    entry2 = DiaryEntry("Entry2", "This is a diffferent entry", two_days_ago)
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    result = diary.read(new_date)
    assert result == ["This is today's entry"]

#4 Diary.read() returns contents of entry filtered on date (mulitple entries)
def test_read_returns_diary_contents_mulitple():
    diary = Diary()
    entry1 = DiaryEntry("Entry1", "This is today's entry", new_date)
    entry2 = DiaryEntry("Entry2", "This is a diffferent entry", two_days_ago)
    entry3 = DiaryEntry("Entry3", "This is a new one", new_date)
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_diary_entry(entry3)
    result = diary.read(new_date)
    assert result == ["This is today's entry", "This is a new one"]
    

    