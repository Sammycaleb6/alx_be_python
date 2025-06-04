from datetime import datetime, timedelta

current_datetime = datetime.now()
print(f"current date and time {current_datetime}")

days_to_add = int(input("Enter the number of days to add: "))

future_date = current_datetime + timedelta(days=days_to_add)
print(f"future date {future_date}")