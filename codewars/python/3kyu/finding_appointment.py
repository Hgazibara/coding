import operator

WORKDAY_START = '09:00'
WORKDAY_END = '19:00'

def get_start_time(schedules, duration):
    events = sorted(sum(schedules, []), key=operator.itemgetter(0))
    prev_event = events[0]

    earliest_start = events[0][0]
    latest_finish = max(events, key=operator.itemgetter(1))[1]

    potential_appointments = []

    if earliest_start != WORKDAY_START:
        potential_appointments.append([WORKDAY_START, earliest_start])

    if latest_finish != WORKDAY_END:
        potential_appointments.append([latest_finish, WORKDAY_END])

    for next_event in events[1:]:
        ps, pe = prev_event
        ns, ne = next_event

        if ns <= pe:
            prev_event = [ps, max(pe, ne)]
        else:
            potential_appointments.append([pe, ns])
            prev_event = next_event

    for start, end in potential_appointments:
        if to_minutes(end) - to_minutes(start) >= duration:
            return start

    return None


def to_minutes(appointment):
    hours, minutes = appointment.split(':')
    return int(hours)*60 + int(minutes)
