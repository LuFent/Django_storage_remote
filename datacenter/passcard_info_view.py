from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.storage_information_view import format_duration
from datacenter.storage_information_view import get_duration
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_raw = Visit.objects.filter(passcard=this_passcard)
    this_passcard_visits = []
    suspiciousness_gap = 3600

    for visit in this_passcard_visits_raw:
        duration = get_duration(visit.entered_at, visit.leaved_at)
        is_suspicious = duration.total_seconds() > suspiciousness_gap

        duration = format_duration(duration)

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_suspicious
        })

    context = {
        'passcard': this_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
