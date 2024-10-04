from math import floor
book_pages = int(input())
pages_per_hour = int(input())
days_for_reading_the_book = int(input())
hours_of_reading_per_day = (book_pages/pages_per_hour) /days_for_reading_the_book
print(floor(hours_of_reading_per_day))
