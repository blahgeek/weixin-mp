from django.shortcuts import render
import json
from django.http import HttpResponse

from vote.models import VoteConfiguration, VoteModel, VotedUserModel

# Create your views here.

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


def index(req):
    return render(req, 'index.html')
