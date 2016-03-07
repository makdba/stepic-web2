from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from .models import Question, Answer
from .utils import paginate


def test(request, *args, **kwargs):
    return HttpResponse("OK")


@require_GET
def index(request):
    paginator, page = paginate(request, Question.objects.order_by('-added_at'))
    return render(request, 'qa/index.html', {
        'page': page,
        'paginator': paginator,
    })


@require_GET
def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers
    })


@require_GET
def popular(request):
    paginator, page = paginate(request, Question.objects.order_by('-rating'))
    return render(request, 'qa/index.html', {
        'page': page,
        'paginator': paginator
    })
