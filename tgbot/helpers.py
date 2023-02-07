from datetime import datetime, timedelta


def clear_data(data: str) -> str:
    return data.strip()


def _get_list_of_weekdays_between_dates(start_date: datetime, end_date: datetime, week_day: int) -> list[datetime]:
    days = (start_date + timedelta(i) for i in range((end_date - start_date).days + 1))
    return [day for day in days if day.weekday() == week_day]


def check_dates(now: datetime, lection_start_datetime: datetime) -> bool:
    for schedule_date in _get_list_of_weekdays_between_dates(lection_start_datetime,
                                                             lection_start_datetime + timedelta(days=90),
                                                             lection_start_datetime.date().weekday()):
        if schedule_date <= now <= schedule_date + timedelta(minutes=95):
            return True
    return False
