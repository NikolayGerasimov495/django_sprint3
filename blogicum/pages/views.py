from django.shortcuts import render


def about(request):
    """Представление страницы о сайте"""
    return render(request, 'pages/about.html')


def rules(request):
    """Представление страницы правил"""
    return render(request, 'pages/rules.html')
