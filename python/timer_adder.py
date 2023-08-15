from datetime import datetime, timedelta


def add_time(time_str, add_time_str):
    time_format = "%I:%M %p"

    # Convert the time_str to a datetime object
    time_obj = datetime.strptime(time_str, time_format)

    # Parse the add_time_str for hours and minutes
    add_hours, add_minutes = map(int, add_time_str.split(":"))

    # Calculate the new time by adding hours and minutes
    new_time = time_obj + timedelta(hours=add_hours, minutes=add_minutes)

    return new_time.strftime("%I:%M %p")


# Test the function
result = add_time("3:00 PM", "13:10")
print("Result:", result)
