from datetime import date,timedelta
dob = date(2001, 1, 20)


def birth_date():
    my_age = (date.today() - dob) // timedelta(days=365.2425)
    return my_age


print(birth_date())




