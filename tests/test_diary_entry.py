from lib.organiser import DiaryEntry
from datetime import datetime, timedelta
import pytest

current_date = datetime.now()
current_date = current_date.date() #remove time
formatted_date = current_date.strftime('%d%m%Y') #format -> str
new_date = datetime.strptime(formatted_date, '%d%m%Y') #strptime -> datetime

two_days_ago = new_date - timedelta(days = 2)


# Unit tests for DiaryEntry


#2 DiaryEntry.word_count() return number of words in selected entry
def test_word_count_returns_length_of_contents():
    entry = DiaryEntry("Entry2", "This is today's entry", new_date)
    result = entry.word_count()
    assert result == 4

#1 raise error if title not str
def test_raise_error_if_title_not_str():
    with pytest.raises(Exception) as e:
        DiaryEntry(1, "This is today's entry", new_date)
    assert str(e.value) == "Arguments must be of type str"

#2 raise error if contents not str
def test_raise_error_if_contents_not_str():
    with pytest.raises(Exception) as e:
        DiaryEntry("entry 1", 43234, new_date)
    assert str(e.value) == "Arguments must be of type str"

#3 raise error if date_added not date object
def test_raise_error_if_date_added_not_date():
    with pytest.raises(Exception) as e:
        DiaryEntry("entry1", "This is today's entry", 12042023)
    assert str(e.value) == "Argument must be of type date"



