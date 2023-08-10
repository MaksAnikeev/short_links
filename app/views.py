from django.shortcuts import render
import secrets
import string
from .models import Links
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .forms import UserForm


def create_links(request):
    """
    Добавление в базу связки длинной и короткой ссылки, если короткая не передана, то генерируем случайную
    """
    full_link = request.GET.get('full_link')
    if request.GET.get('short_link'):
        short_link = f"link/{request.GET.get('short_link')}"
        if Links.objects.filter(short_link=short_link).exists():
            response = {
                'message': 'такая короткая ссылка уже существует, введите другую'
            }
            return JsonResponse(
                response,
                status=500,
                json_dumps_params={'ensure_ascii': True}
            )
    else:
        while True:
            letters_and_digits = string.ascii_letters + string.digits
            random_word = ''.join(secrets.choice(letters_and_digits) for i in range(10))
            short_link = f'link/{random_word}'
            if not Links.objects.filter(short_link=short_link).exists():
                break
    Links.objects.create(
        full_link=full_link,
        short_link=short_link
    )
    response = {
        'short_link': short_link,
        'message': 'объект создан'
        }
    return JsonResponse(
        response,
        status=200,
        json_dumps_params={'ensure_ascii': True}
    )


def redirect_link(request, short_link):
    """
    Перенаправление короткой ссылки на длинную
    """
    link = get_object_or_404(Links, short_link=f'link/{short_link}')
    link.clicks_count += 1
    link.save()
    return redirect(link.full_link)



def index_page(request):
    """
    Создание короткой ссылки на странице сайта
    """
    submitbutton = request.POST.get("submit")

    form = UserForm(request.POST or None)
    if form.is_valid():
        full_link = form.cleaned_data.get("full_link")
        short_link = form.cleaned_data.get("short_link")
    else:
        context = {'form': form,
                   'short_link': 'введена не корректная информация',
                   'submitbutton': submitbutton,
                   }
        return render(request, 'index.html', context)

    if short_link:
        short_link = f"link/{short_link}"
        if Links.objects.filter(short_link=short_link).exists():
            context = {'form': form,
                       'short_link': 'такая короткая ссылка уже существует, введите другую',
                       'submitbutton': submitbutton,
                       }
            return render(request, 'index.html', context)
    else:
        while True:
            letters_and_digits = string.ascii_letters + string.digits
            random_word = ''.join(secrets.choice(letters_and_digits) for i in range(10))
            short_link = f'link/{random_word}'
            if not Links.objects.filter(short_link=short_link).exists():
                break

    Links.objects.create(
        full_link=full_link,
        short_link=short_link
    )

    context = {'form': form,
               'short_link': short_link,
               'submitbutton': submitbutton,
               }

    return render(request, 'index.html', context)
