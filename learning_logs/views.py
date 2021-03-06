from django.shortcuts import render, redirect
from .models import Topic

from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """show individual topic and all it's entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        """No data submited create a blank form"""
        form = TopicForm()

    else:
        # If POST data is submited process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics_link')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)



def new_entry(request, topic_id):
    """Add a new topic for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        """No data submited create a new form"""
        form = EntryForm()
    else:
        # POST dats submited process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.entry.save()
            return redirect('topic')

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)












    