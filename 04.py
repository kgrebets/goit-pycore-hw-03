import datetime

def get_upcoming_birthdays(users):
    now = datetime.datetime.today().date()
    upcoming_birthdays = []
    
    try:
        for user in users:
            original_birthday = datetime.datetime.strptime(user['birthday'], "%d.%m.%Y").date()
            
            birthday_this_year = original_birthday.replace(year=now.year)
            
            is_birthday_yesterday_but_sunday_today = (now.weekday() == 6) and (now == birthday_this_year + datetime.timedelta(days=1))

            if birthday_this_year < now:
                birthday_this_year = birthday_this_year.replace(year=now.year + 1)
            
            till_birthday_days = (birthday_this_year - now).days

            congratulation_date = None
            if (0 <= till_birthday_days <= 7):
                congratulation_date = birthday_this_year

                if birthday_this_year.weekday() in (5,6): #saturday, sunday
                    days_till_monday = 7 - birthday_this_year.weekday()
                    congratulation_date = birthday_this_year + datetime.timedelta(days=days_till_monday)
               
            elif is_birthday_yesterday_but_sunday_today:
                congratulation_date = now + datetime.timedelta(days=1)
            else:
                continue
           
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y-%m-%d")
            })
        
        return upcoming_birthdays
    except Exception as e:
        print(f"An error occurred: {e}")  

users = [
    {"name": "Victor", "birthday": "05.07.1992"}, #passed does not meet condition
    {"name": "Nadia",  "birthday": "06.07.1993"}, #passed but saturday
    {"name": "Helga",  "birthday": "07.07.1991"}, #date of run
    {"name": "Mary",  "birthday": "08.07.1990"}, #future
    {"name": "Alex",   "birthday": "13.07.1990"}, #future saturday
    {"name": "Sasha",  "birthday": "29.07.1990"}  #does not meet condition
]

for x in get_upcoming_birthdays(users):
    print(x)

