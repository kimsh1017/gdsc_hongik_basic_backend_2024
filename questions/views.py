from django.shortcuts import render,redirect
from questions.models import Question
from django.utils import timezone

# Create your views here.
def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question' : question}
    return render(request, 'question_detail.html', context)

def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'question_list.html', context)

def question_create(request):
    if request.method == 'GET':
        return render(request, 'question_create.html')
    elif request.method == 'POST':
        Question.objects.create(
            subject = request.POST["subject"],
            content = request.POST["content"],
            create_date = timezone.now()
        )
        return redirect('/questions')