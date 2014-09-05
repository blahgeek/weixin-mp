from django.shortcuts import render
import json
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods

from django.shortcuts import redirect

from vote.models import VoteConfiguration, VoteModel, VotedUserModel

# Create your views here.

@staff_member_required
def getJson(req):
    conf = VoteConfiguration.objects.get()
    values = map(lambda x: [x.candidate, x.count], VoteModel.objects.all())
    user_count = VotedUserModel.objects.count()
    ret = {
        'title': conf.vote_name,
        'values': values,
        'user_count': user_count,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')


@staff_member_required
def index(req):
    return render(req, 'index.html')


@staff_member_required
def delete(req):
    return render(req, 'confirm_delete.html')


@staff_member_required
@require_http_methods(['POST', ])
def real_delete(req):
    VoteModel.objects.all().delete()
    VotedUserModel.objects.all().delete()
    return redirect('vote.index')
