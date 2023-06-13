from lib.organiser import Organiser, DiaryEntry
from datetime import datetime, timedelta

current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
two_days_ago = current_date - timedelta(days = 2)

#integration Organiser and DiaryEntry

#1 Organiser.diary_entries returns list of diary entry objects ordered by date added in descending order.
def test_diary_entries_returns_list_ordered_by_date():
    organiser = Organiser()
    entry1 = DiaryEntry("Entry1", "This is my first diary entry", yesterday)
    entry2 = DiaryEntry("Entry2", "This is today's entry", current_date)
    organiser.add_diary_entry(entry1)
    organiser.add_diary_entry(entry2)
    result = organiser.all_diary_entries()
    assert result == [entry2, entry1]

#2 Organiser.reading_time returns best diary entry to read for the given time and speed.
def test_reading_time_returns_best_diary_entry():
    organiser = Organiser()
    entry1 = DiaryEntry("Entry1", "This is my first diary entry, this is a much longer one I will keep going blah blah blah", yesterday)
    entry2 = DiaryEntry("Entry2", "This is today's entry", current_date)
    organiser.add_diary_entry(entry1)
    organiser.add_diary_entry(entry2)
    result = organiser.reading_time(10, 2)
    assert result == entry1

#3 Organiser.return_contacts returns list of mobile phone numbers from all diary entries sorted by date_added in decending order.
def test_return_contacts_returns_list_of_diary_phone_numbers():
    organiser = Organiser()
    entry1 = DiaryEntry("Entry1", "This is my first diary entry, today I met my friend Lucy her number is 08987654321", two_days_ago)
    entry2 = DiaryEntry("Entry2", "This is another entry", yesterday)
    entry3 = DiaryEntry("Entry2", "This is today's entry, today I met Tom: 09856789034", current_date)
    organiser.add_diary_entry(entry1)
    organiser.add_diary_entry(entry2)
    organiser.add_diary_entry(entry3)
    result = organiser.return_contacts()
    assert result == ['09856789034', '08987654321']

