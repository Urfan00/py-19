from django.shortcuts import render


def home(request):
    return render(request, 'home.html')



def staff(request):

    ctx = {
        "isci": 'Murad',
        "yas": 25,
        "is_student": False,
        "ball": 70.5,
        "diller": ["Python", "C++", "Java"]
    }


    return render(request, 'staff.html', ctx)

