import datetime

class EnhancedDate:
    def _init_(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            now = datetime.datetime.utcnow()
            self._date_time = now.replace(hour=hour, minute=minute, second=second)
        else:
            self._date_time = datetime.datetime(year, month, day, hour, minute, second)

    @classmethod
    def from_standard_format(cls, standard_string):
        try:
            temp_date = datetime.datetime.fromisoformat(standard_string)
            return cls(temp_date.year, temp_date.month, temp_date.day, temp_date.hour, temp_date.minute, temp_date.second)
        except ValueError as error:
            raise ValueError(f"Incorrect ISO format: {standard_string}") from error

    def to_standard_format(self):
        return self._date_time.isoformat()

    def to_readable_format(self):
        return self._date_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def check_date_validity(year, month, day):
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def difference_between_dates(cls, first_date, second_date, measurement='days'):
        if not isinstance(first_date, cls) or not isinstance(second_date, cls):
            raise ValueError("Both parameters must be EnhancedDate instances")
        
        time_delta = first_date._date_time - second_date._date_time

        if measurement == 'days':
            return time_delta.days
        elif measurement == 'weeks':
            return time_delta.days // 7
        elif measurement == 'months':
            return (first_date.year - second_date.year) * 12 + first_date.month - second_date.month
        else:
            raise ValueError("Invalid measurement. Use 'days', 'weeks', or 'months'.")

    @staticmethod
    def create_from_string(input_string):
        try:
            parsed_date = datetime.datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S")
            return EnhancedDate(parsed_date.year, parsed_date.month, parsed_date.day, parsed_date.hour, parsed_date.minute, parsed_date.second)
        except ValueError as error:
            raise ValueError(f"Wrong format for date string: {input_string}") from error

    # Properties for accessing datetime components
    @property
    def year(self):
        return self._date_time.year

    @property
    def month(self):
        return self._date_time.month

    @property
    def day(self):
        return self._date_time.day

    @property
    def hour(self):
        return self._date_time.hour

    @property
    def minute(self):
        return self._date_time.minute

    @property
    def second(self):
        return self._date_time.second
    
# Example of how to use the class
# Instantiating objects with various approaches
date1 = EnhancedDate(2023, 1, 1, 12, 30, 45)
date2 = EnhancedDate.from_standard_format("2023-01-01T12:30:45")

# Displaying dates in different formats
print("Standard ISO Format:", date1.to_standard_format())
print("Readable Date Format:", date1.to_readable_format())

# Getting individual components of a date
print("Extracted Year:", date1.year)
print("Extracted Month:", date1.month)
print("Extracted Day:", date1.day)
print("Extracted Hour:", date1.hour)
print("Extracted Minute:", date1.minute)
print("Extracted Second:", date1.second)

# Checking date validity
print("Checking 2023-01-01 for validity:", EnhancedDate.check_date_validity(2023, 1, 1))
print("Checking 2023-02-30 for validity:", EnhancedDate.check_date_validity(2023, 2, 30))

# Calculating the difference between two dates
date3 = EnhancedDate(2023, 1, 10)
print("Days Between Dates:", EnhancedDate.difference_between_dates(date1, date3, measurement='days'))
print("Weeks Between Dates:", EnhancedDate.difference_between_dates(date1, date3, measurement='weeks'))
print("Months Between Dates:", EnhancedDate.difference_between_dates(date1, date3, measurement='months'))

# Creating a date object from a string
date4 = EnhancedDate.create_from_string("2023-03-15 08:45:30")
print("Date From String:", date4.to_readable_format())
