#sample data
SCHEDULE = {
    "monday": "Class 10 am to 12 pm. Part-time work 2 pm to 6 pm.",
    "tuesday": "Free day.",
    "wednesday": "Class 10 am to 12 pm. Study group at 4 pm.",
    "thursday": "Part-time work 9 am to 1 pm.",
    "friday": "Free day.",
    "saturday": "Grocery shopping in the morning.",
    "sunday": "Free day.",
}

DEADLINES =[
    "Deep Learning Homework: due thursday",
    "Artificial Intelligence Assignment: due thursday",
    "Machine Learning Project report: due sunday",]

def get_schedule(day:str)->str:
    """R Returns the user's plan for one day of the week, for example 'monday'."""
    return SCHEDULE.get(day.lower(), "No plans found for that day.")

def get_deadlines() -> list[str]:
    """Returns the user's upcoming assignment deadlines."""
    return DEADLINES