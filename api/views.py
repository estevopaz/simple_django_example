import datetime
import json
import logging

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from api.models import New


LOGGER = logging.getLogger(__name__)


# Create your views here.

def index(request):
    '''
    API index.
    '''
    return HttpResponse('API index, please choose the right path !')


def add_new(request):
    '''
    Create a new "New" instance.
    '''
    if request.method == 'POST':
        try:
            ############ XXX: Only for debugging; DELETE ME
            print('Remove me from source code !')
            from IPython.core.debugger import Tracer
            Tracer('Linux')()
            ############# XXX: Only for debugging; DELETE ME
            json_data = json.loads(request.body.decode('utf8'))

            # Authentication
            user = authenticate(username=json_data['user'],
                                password=json_data['pass'])
            if not user.is_authenticated():
                raise RuntimeError('Authentication error !')

            # Create new "New"
            new = New(title=json_data['title'],
                      body=json_data['body'],
                      pub_date=json_data['pub_date'])
            new.save()
            return HttpResponse('New titled: "{}" created successfully !'
                                .format(json_data['title']))
        except Exception as error:
            error = '{}: {}'.format(error.__class__.__name__, error)
            LOGGER.error(error)
            return HttpResponse(error)
    else:
        return HttpResponse('ERROR: This API requires a POST call !')


def news(request):
    '''
    Get recent "News".
    '''
    latest = 10
    
    news_recent = New.objects.order_by('-pub_date')[:latest]
    template = loader.get_template('news.html')
    context = {
        'news': news_recent,
    }
    return HttpResponse(template.render(context, request))
