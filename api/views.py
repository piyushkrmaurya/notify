from django.shortcuts import render

def home(request):
    name = request.GET.get("name", None)
    if name:
        return render(request, "home.html", {"name": name})
    else:
        return render(request, "home.html")