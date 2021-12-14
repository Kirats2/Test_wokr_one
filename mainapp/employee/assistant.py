from datetime import datetime


def experience(date):
    d1 = datetime.now()
    d2 = date
    time = ((d1.year - d2.year) * 12 + d1.year - d2.year) // 12
    if time < 20:
        if time == 1:
            return f' {time} год'
        elif time in [2, 3, 4]:
            return f' {time} года'
        else:
            return f'{time} лет'
    else:
        if str(time)[-1] == '1':
            return f' {time} год'
        elif str(time)[-1] in ['2', '3', '4']:
            return f' {time} года'
        else:
            return f'{time} лет'
