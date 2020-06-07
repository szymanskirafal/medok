from django.utils import timezone


def check_shift():
    now = timezone.now()
    if now.hour > 16:
        if now.hour > 17:
            shift = "night"

        else:
            if now.minute > 29:
                shift = "night"
            else:
                shift = "day"
    else:
        shift = "day"
    return shift
