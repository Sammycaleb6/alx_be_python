from datetime import datetime, timedelta

def display_current_datetime():
  current_datetime = datetime.now()
  print(f"current date and time {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

display_current_datetime()
def calculate_future_date():
  current_datetime = datetime.now()
  days_to_add = int(input("Enter the number of days to add to the current date: "))

  future_date = current_datetime + timedelta(days=days_to_add)
  print(f"future date {future_date.strftime('%Y-%m-%d')}")
calculate_future_date()