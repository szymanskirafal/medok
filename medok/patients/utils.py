from django.utils import timezone


def check_shift():
    now = timezone.now()
    print("we here")
    print("now is: ", now)
    print("now hour is: ", now.hour)
    print("now minute is: ", now.minute)
    if now.hour > 16:
        print("now.hour is ", now.hour)
        if now.hour > 17:
            shift = "night"

        else:
            print("now.hour is ", now.hour)
            print("now.minute is ", now.minute)
            if now.minute > 29:
                shift = "night"
            else:
                shift = "day"
    else:
        shift = "day"
    print("#### check shift returns ", shift)
    return shift
