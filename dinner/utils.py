import datetime
from dateutil import rrule

# To select when to go to the next week, choose 5 for saturday
LAST_DAY_OF_WEEK = 5


def get_days_range(date=None, days=7):
    '''
    Get the begin and end date of the week (including the next day for easy
    filtering with Django)
    '''
    if not date:
        date = datetime.date.today()

    day_of_week = date.weekday()
    if day_of_week >= LAST_DAY_OF_WEEK:
        day_of_week = -7

    to_beginning_of_week = datetime.timedelta(days=day_of_week)
    beginning_of_week = date - to_beginning_of_week

    to_end_of_week = datetime.timedelta(days=days - day_of_week)
    end_of_week = date + to_end_of_week

    return beginning_of_week, end_of_week


def get_days_from(date=None, days=7):
    '''Get a datetime object for every day of the week'''
    start_date, _ = get_days_range(date, days=days)
    return (day.date() for day in rrule.rrule(
        rrule.DAILY,
        start_date,
        count=days,
    ))


def get_days(start_date, end_date):
    '''Get a datetime object for every day of the week'''
    return [day.date() for day in rrule.rrule(
        rrule.DAILY,
        start_date,
        until=end_date,
    )]

