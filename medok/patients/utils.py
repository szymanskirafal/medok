from django.utils import timezone


def check_shift():
    now = timezone.now()
    print("we here")
    print("now is: ", now)
    print("now hour is: ", now.hour)
    print("now minute is: ", now.minute)
    if now.hour > 16:
        print("now.hour is ", now.hour)
        if now.hour > 18:
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
    return shift
