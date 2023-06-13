from lib.organiser import DiaryEntry
from datetime import datetime

current_date = datetime.now()

# Unit tests for DiaryEntry

# DiaryEntry.word_count() return number of words in selected entry

def test_word_count_returns_length_of_contents():
    entry = DiaryEntry("Entry2", "This is today's entry", current_date)
    result = entry.word_count()
    assert result == 4


#1 raise error if title not str

#2 raise error if contents not str

#3 raise error if date_added not in correct format

#4 DiaryEntry.read returns contents of entry

