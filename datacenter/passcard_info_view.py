from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.storage_information_view import format_duration
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_raw = Visit.objects.filter(passcard=this_passcard)
    this_passcard_visits = []
    now = localtime()
    suspiciousness_gap = 3600

    for visit in this_passcard_visits_raw:

        if visit.leaved_at:
            raw_duration = visit.leaved_at - visit.entered_at
        else:
            raw_duration = now - visit.entered_at

        duration = format_duration(raw_duration)

        is_suspicious = raw_duration.total_seconds() > suspiciousness_gap

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
