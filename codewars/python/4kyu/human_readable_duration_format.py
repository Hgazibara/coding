def format_duration(seconds):
    if seconds == 0:
        return 'now'

    labels = ['year', 'day', 'hour', 'minute', 'second']
    amounts = [365*24*3600, 24*3600, 3600, 60, 1]

    output = []

    for amount, label in zip(amounts, labels):
        x, y = divmod(seconds, amount)
        if x > 0:
            output.append('{0} {1}{2}'.format(x, label, 's' if x >= 2 else ''))
        seconds = y

    return ', '.join(output)[::-1].replace(' ,', ' dna ', 1)[::-1]
