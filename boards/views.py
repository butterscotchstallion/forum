from django.shortcuts import render

def board_list(request):
    return render(request, 'boards/index.html')
