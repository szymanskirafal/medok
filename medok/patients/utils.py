from django.utils import timezone


def check_shift():
    now = timezone.now()
    print("we here")
    if now.hour > 17:
        if now.hour > 18:
            shift = "night"

        else:
            if now.minute > 29:
                shift = "night"
            else:
                shift = "day"
    else:
        shift = "day"
    return shift
