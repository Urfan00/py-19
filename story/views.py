from story.models import Story
from django.shortcuts import render


def stories(request):

    stories = Story.objects.all()

    context = {
        'all_stories': stories
    }

    return render(request, 'stories.html', context)


