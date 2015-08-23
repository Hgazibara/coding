def make_readable(seconds):
    hours, remaining = divmod(seconds, 3600)
    minutes, seconds = divmod(remaining, 60)
    return ':'.join(convert(__) for __ in [hours, minutes, seconds])

def convert(amount):
    return '{0:02d}'.format(amount)
