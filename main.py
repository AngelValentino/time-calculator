def add_time(start, duration, day = None):
    # Convert time to to a 24-hour format in minutes
    def convert_to_minutes(time):
        # 12-hour clock format
        if 'AM' in time or 'PM' in time:
            # Split time string and meridiem
            time_str, meridiem = time.split()
            # Split hours and minutes and convert them to integers
            hours, minutes = map(int, time_str.split(':'))

            # Convert to 24-hour format in minutes
            if meridiem == 'PM' and hours != 12:
                # If the time is in the PM period and the hour is not 12, 
                # 12 hours are added to convert it to a 24-hour format
                hours += 12
            elif meridiem == 'AM' and hours == 12:
                # If the time is in the AM period and the hour is 12, 
                # the hour is set to 0 to represent midnight in 24-hour format
                hours = 0
            # return the total minutes since midnight 
            return hours * 60 + minutes
        # Added time
        else:
            # Split hours and minutes and convert them to integers
            hours, minutes = map(int, time.split(':'))
            # return the total minutes since midnight 
            return hours * 60 + minutes

    # Convert minutes to 12-hour clock format
    def convert_to_12_hour(minutes):
        # Calculate total hours and wrap around at 24 hours
        hours = (minutes // 60) % 24
        # Rmaining minutes within an hour
        minutes = minutes % 60

        if hours == 0:
            # If hours are 0 it represent midnight in 12-hour clock format so hours are set to 12 AM
            meridiem = 'AM'
            hour_12 = 12
        elif 1 <= hours < 12:
            # If hours are between 1 and 12 set hours as they are with AM
            meridiem = 'AM'
            hour_12 = hours
        elif hours == 12:
            # If hours are 12 set the hours to be 12 PM
            meridiem = 'PM'
            hour_12 = 12
        else:
            # Else for hours between 12 and 23 remove 12 from the hours and add PM
            meridiem = 'PM'
            hour_12 = hours - 12

        # return time in 12-hour clock format 'h:mm M'
        return f"{hour_12}:{minutes:02} {meridiem}"

    # Convert both times to minutes
    start_minutes = convert_to_minutes(start)
    added_duration_minutes = convert_to_minutes(duration)

    # Calculate the total minutes
    total_minutes = start_minutes + added_duration_minutes

    # Calculate the number of days passed
    # Divides the total minutes by 1440 (the number of minutes in a day)
    days_passed = total_minutes // 1440
    # Calculate the remaining minutes after accounting for the full days
    remaining_minutes = total_minutes % 1440

    # Convert remaining minutes back to a 12-hour clock format
    formatted_time = convert_to_12_hour(remaining_minutes)

    # Handle the day of the week if provided
    if day:
        # List of days in a week, starting from Monday
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # Find the index of the provided day in the days_of_week list
        current_day_index = days_of_week.index(day.capitalize())
        # Calculate the new day index by adding the number of days passed and 
        # using modulus 7 to wrap around the week
        new_day_index = (current_day_index + days_passed) % 7
        # Determine the new day of the week based on the new index
        new_day = days_of_week[new_day_index]
        # Append the new day of the week to the formatted time string
        formatted_time += f", {new_day}"

    # Append the number of days passed if more than zero
    if days_passed == 1:
        # One day has passed
        formatted_time += " (next day)"
    elif days_passed > 1:
        # More than one day has passed
        formatted_time += f" ({days_passed} days later)"

    return formatted_time

# Examples
print(add_time('3:00 PM', '3:10'))
# Expected: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Expected: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Expected: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Expected: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Expected: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Expected: 7:42 AM (9 days later)