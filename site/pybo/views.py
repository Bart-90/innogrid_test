from django.shortcuts import render
from .models import world

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