from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import world
from django.shortcuts import render
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed


# 메인 페이지
def index(request):
    worlds = world.objects
    return render(request, 'pybo/main_page.html', {'worlds': worlds} )

def detail(request, world_id):
    wi = world.objects.get(id=world_id)
    p1 = world.objects.get(id=world_id)
    p2 = world.objects.get(id=world_id)
    p3 = world.objects.get(id=world_id)
    p4 = world.objects.get(id=world_id)
    p5 = world.objects.get(id=world_id)
    p6 = world.objects.get(id=world_id)
    p7 = world.objects.get(id=world_id)
    p8 = world.objects.get(id=world_id)
    context = {'wi': wi, 'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5, 'p6': p6, 'p7': p7, 'p8': p8}
    return render(request, 'pybo/reserv_form.html', context)

def reservation(request, world_id):
    worlds = world.objects
    context = {'worlds': worlds}
    return render(request, 'pybo/main_page.html', context)

def index1(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail1(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail1', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index1')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

def notification(request):
    context = {}
    return render(request, 'pybo/notification.html', context)

def QnA(request):
    context = {}
    return render(request, 'pybo/QnA.html', context)