import calendar
from datetime import datetime

def generate_calendar(date_list: list[str]) -> str:
    if not date_list:
        raise ValueError("Дата список пуст")

    # Преобразуем строки в datetime объекты
    parsed_dates = [datetime.strptime(d, "%d-%m-%Y") for d in date_list]

    # Все даты должны быть из одного месяца
    month = parsed_dates[0].month
    year = parsed_dates[0].year
    if any(d.month != month or d.year != year for d in parsed_dates):
        raise ValueError("Все даты должны быть из одного месяца и года")

    # Получим дни, которые нужно выделить
    highlight_days = set(d.day for d in parsed_dates)

    # Заголовок
    header = f"Календарь активностей для {year}-{month:02}:\n"
    days_header = "Пн Вт Ср Чт Пт Сб Вс\n"

    # Календарь начинается с понедельника
    cal = calendar.Calendar(firstweekday=0)
    weeks = cal.monthdayscalendar(year, month)

    lines = []
    for week in weeks:
        line = ""
        for day in week:
            if day == 0:
                line += "   "
            elif day in highlight_days:
                line += "✅ "
            elif day < 10:
                line += f"{day}  "
            else:
                line += f"{day} "
        lines.append(line.rstrip())

    return header + days_header + "\n".join(lines)
