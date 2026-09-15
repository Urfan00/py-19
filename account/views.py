from django.shortcuts import render


def user_list(request):

    context = {
        'title': 'PY-19',
        'count': 10,
        'users': ['Urfan', 'Xeyyam', 'Araz']
    }

    return render(request, 'user_list.html', context)
