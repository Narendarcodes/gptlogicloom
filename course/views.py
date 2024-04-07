from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import escape
from profilepage.models import Profile
from .models import Answers,userprogress
from django.contrib.auth.models import AnonymousUser,User

def course2content(request):
    return render(request, "course/course2/content.html")

def course1content(request):
    return render(request, "course/course1/content.html")

def course1(request, slug):
    topics = Answers.objects.filter(topic__startswith='c1')
    chapters = {}

    # Group topics by chapters
    for topic in topics:
        # Parse topic name to extract chapter and topic numbers
        _, chapter_topic = topic.topic.split('ch')
        chapter, topic_number = chapter_topic.split('t')

        # Create chapter key if not exists
        if chapter not in chapters:
            chapters[chapter] = []

    # Append topic information to the corresponding chapter
        chapters[chapter].append({
          'chapter': chapter,
          'topic': topic_number,
          'topicid':topic.topic,
          'topic_text': topic.topictext,
          'completed': istopiccompleted(topic.topic, request)  # Assuming you have a field to indicate completion status
        })
    context = {'chapters': chapters}
    return render(request, f"course/course1/{slug}.html",context)

def course2(request, slug):
    topics = Answers.objects.filter(topic__startswith='c2')
    chapters = {}

    # Group topics by chapters
    for topic in topics:
        # Parse topic name to extract chapter and topic numbers
        _, chapter_topic = topic.topic.split('ch')
        chapter, topic_number = chapter_topic.split('t')

        # Create chapter key if not exists
        if chapter not in chapters:
            chapters[chapter] = []

    # Append topic information to the corresponding chapter
        chapters[chapter].append({
          'chapter': chapter,
          'topic': topic_number,
          'topicid':topic.topic,
          'topic_text': topic.topictext,
          'completed': istopiccompleted(topic.topic, request)  # Assuming you have a field to indicate completion status
        })
        # Sort topics by chapter and topic
    for chapter in chapters.values():
        chapter.sort(key=lambda x: (int(x['chapter']), int(x['topic'])))

    # Sort chapters by chapter number
    chapters = dict(sorted(chapters.items(), key=lambda item: int(item[0])))
    context = {'chapters': chapters}
  
    return render(request, f"course/course2/{slug}.html", context)


def istopiccompleted(topic,request):
    if isinstance(request.user,AnonymousUser):
        return False
    elif isinstance(request.user,User):
        user_progress = userprogress.objects.filter(user=request.user, completed_topic__topic=topic)
        return user_progress.exists()

def checkanswerc2(request, slug):
    if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        validslug = escape(slug)

        answers = Answers.objects.filter(topic=validslug).first()
        if answers:
            if option1 == answers.que1 and option2 == answers.que2:
                if isinstance(request.user,AnonymousUser):
                 messages.warning(request,"Well Done! That was Awesome response Please Login to save your progress")
                elif isinstance(request.user,User):
                 user_profile = Profile.objects.filter(user=request.user).first()
                 user_progress,_ = userprogress.objects.get_or_create(user=request.user)
                 user_progress.completed_topic.add(answers)
                 user_profile.c2progress = getprogress(request,'c2')
                 user_profile.save()
                 user_progress.save()
                 messages.success(request, f"Well Done! {user_profile.name} That was an Awesome response")
            else:  
                messages.error(request, "Wrong Answers. Try Again!")
        else:
            return redirect("home")
        
        return redirect(f"../../course2/{slug}")

def checkanswerc1(request, slug):
   if request.method == 'POST':
        option1 = request.POST.get("q1")
        option2 = request.POST.get("q2")
        
        validslug = escape(slug)

        answers = Answers.objects.filter(topic=validslug).first()
        if answers:
            if option1 == answers.que1 and option2 == answers.que2:
                if isinstance(request.user,AnonymousUser):
                 messages.warning(request,"Well Done! That was Awesome response Please Login to save your progress")
                elif isinstance(request.user,User):
                 user_profile = Profile.objects.filter(user=request.user).first()
                 user_progress,_ = userprogress.objects.get_or_create(user=request.user)
                 user_progress.completed_topic.add(answers)
                 user_profile.c1progress = getprogress(request,'c1')
                 user_profile.save()
                 user_progress.save()
                 messages.success(request, f"Well Done! {user_profile.name} That was an Awesome response")
            else:  
                messages.error(request, "Wrong Answers. Try Again!")
        else:
            return redirect("home")
        
        return redirect(f"../../course1/{slug}")
    
def getprogress(request, course):
    user_progress = userprogress.objects.filter(user=request.user, completed_topic__topic__startswith=course)
    completed_topics = user_progress.count()
    total_topics = Answers.objects.filter(topic__startswith=course).count()
    progress = (completed_topics / total_topics) * 100 if total_topics > 0 else 0
    return progress
