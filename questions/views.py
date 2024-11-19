from django.shortcuts import render,redirect
from questions.models import Question, Answer
from django.utils import timezone

# Create your views here.
def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question = question)
    context = {'question' : question, 'answers': answers}
    return render(request, 'question_detail.html', context)

def question_list(request):
    keyword = request.GET.get('keyword', '')
    questions = Question.objects.filter(subject__icontains = keyword) | Question.objects.filter(content__icontains = keyword)
    context = {'questions': questions, 'keyword': keyword}
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

def question_delete(request, question_id):
    question = Question.objects.get(id = question_id)
    question.delete()
    return redirect('/questions')

def question_update(request, question_id):
    question = Question.objects.get(id = question_id)
    if request.method == 'GET':
        context = {'question' : question}
        return render(request, 'question_update.html', context)

    if request.method == 'POST':
        question.subject = request.POST['subject']
        question.content = request.POST['content']
        question.save()
        return redirect(f'/questions/{question_id}')

def answer_create(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        Answer.objects.create(
            question = question,
            content = request.POST['content'],
            create_date = timezone.now()
        )
        return redirect(f'/questions/{question_id}')