from django.shortcuts import render, get_object_or_404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
#context = DATA
# context = {
#   'recipe': {
#     'яйца': 1,
#     'яблоки': 55,
#   }
# }

from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
from os import listdir


def home_view_1(request):
    template_name = 'calculator/index.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    # pages = {
    #     'Ингридиенты': reverse('home1'),
    #     'Показать омлет': reverse('omlet'),
    #     'Показать паста': reverse('pasta')
    # }
    #
    # # context и параметры render менять не нужно
    # # подбробнее о них мы поговорим на следующих лекциях
    # context = {
    #     'pages': pages,
    #     'DATA': DATA,
    # }
    return render(request, template_name, {'recipe': DATA, 'total':1})
    #return render(request, template_name, context)
    #return HttpResponse(pages)
def omlet_view(request):
    total = int(request.GET.get("servings", 1))
    print(total)
    template_name = 'calculator/index.html'
    #ingridient = DATA['omlet']
    ingridient = {key: value * total for key, value in DATA['omlet'].items()}

    return render(request, template_name, {'recipe': ingridient, 'total': total})


def pasta_view(request):
    template_name = 'calculator/index.html'
    name = DATA['pasta']
    total = int(request.GET.get("servings", 1))
    name = {key: value * total for key, value in DATA['pasta'].items()}

    return render(request, template_name, {'recipe': name})

# def ingr_list(request):
#     ingridients = DATA.values()
#     # по аналогии с `time_view`, напишите код,
#     # который возвращает список файлов в рабочей
#     # директории
#     return HttpResponse(ingridients)
#
# def ingr_details(request, ingr_id):
#     ingridient = get_object_or_404(DATA, id=DATA[ingr_id])
#     template_name = 'calculator/details.html'
#     return render(request, template_name, {'item': ingridient})