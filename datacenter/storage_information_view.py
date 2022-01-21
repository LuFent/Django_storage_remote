from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def format_duration(duration):
    seconds = duration.seconds
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    return f"{hours}ч {minutes}мин"


def get_duration(visit_time):
    now = localtime()
    time_in_storage = now - visit_time
    return time_in_storage


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        visitor_name = visit.passcard
        utc_time_entered = visit.entered_at
        msk_time_entered = localtime(utc_time_entered)
        raw_duration = get_duration(msk_time_entered)
        duration = format_duration(raw_duration)

        non_closed_visits.append({
            'who_entered': visitor_name,
            'entered_at': msk_time_entered,
            'duration': duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
