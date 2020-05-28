from datetime import timedelta

from django.utils import timezone


def check_shift():
    now_in_warsaw = timezone.now() + timedelta(hours=2)
    if now_in_warsaw.hour > 19:
        if now_in_warsaw.hour > 20:
            shift = "night"
        else:
            if now_in_warsaw.minute > 29:
                shift = "night"
    else:
        shift = "day"
    return shift
