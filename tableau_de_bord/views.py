from django.shortcuts import render

def home_view(request):
    return render(request, 'tableau_de_bord/home.html')  # Template pour le tableau de bord
