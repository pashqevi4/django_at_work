from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month} / {year} <br> {text}")


def post_detail(request, year, month, slug):
    ...
    # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем,"
                   " какой способ создания списков в Python работает быстрее..."}
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': 'John'}
    return render(request, 'tst_03_app/my_template.html', context)


class TemplIf(TemplateView):
    template_name = "tst_03_app/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'tst_03_app/templ_for.html', context)


def index(request):
    return render(request, 'tst_03_app/index.html')


def about(request):
    return render(request, 'tst_03_app/about.html')
