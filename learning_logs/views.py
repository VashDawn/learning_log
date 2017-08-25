from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm

# Create your views here.

from learning_logs.models import Topic


def index(request):
    """Main page of learning_log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show single topic and all of it's entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # No data, create a new form.
        form = TopicForm()
    else:
        # POST data, prodess with the data.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add new entry to a specified topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data, create a empty form
        form = EntryForm()
    else:
        # POST data, process with the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
