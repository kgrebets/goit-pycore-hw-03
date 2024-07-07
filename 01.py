from datetime import datetime

def get_days_from_today(input_date):
        now = datetime.today().date()
        delta = now - input_date
        
        if input_date > now:
            (from_date, to_date) =  input_date, now
        else:
            (from_date, to_date) =  now, input_date
        return (from_date, to_date, delta.days)

date_obj = None
while date_obj is None:
    date_str = input("Please enter a date (YYYY-MM-DD format): ")
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")

(from_date, to_date, days) = get_days_from_today(date_obj)

print(f"The difference between {from_date} - {to_date} {abs(days)} days")

# 2020-03-20  2025-12-25