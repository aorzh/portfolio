from django.shortcuts import render_to_response
from django.template import RequestContext
from examples.models import Project


def index(request):
    context_dict = {}
    projects = Project.objects.all()
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict['projects'] = projects
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)
