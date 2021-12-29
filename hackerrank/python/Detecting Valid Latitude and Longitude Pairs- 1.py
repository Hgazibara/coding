import sys

N = sys.stdin.readline()

def is_digit_first(string):
    digits = [str(x) for x in range(1,10)]
    if string[0] == '-' or string[0] == '+':
        return string[1] in digits
    else:
        return string[0] in digits

def is_digit_last(string):
    digits = [str(x) for x in range(0,10)]
    return string[-1] in digits
    
for line in sys.stdin:
    lat, lng = line.replace('\n', '').split(',')
    lat = lat[1:]
    lng = lng[1:-1]
    try:
        latf = float(lat)
        lngf = float(lng)
        
        if not ((-90 <= latf <= 90) and (-180 <= lngf <= 180)):
            print('Invalid')
        else:
            if is_digit_first(lat) and is_digit_first(lng) and is_digit_last(lat) and is_digit_last(lng):
                print('Valid')
            else:
                print('Invalid')
        
    except:
        print('Invalid')