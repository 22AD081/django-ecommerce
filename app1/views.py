from django.http import HttpResponse
from django.template import loader
def example_views(request):
    template=loader.get_template('example.html')
    return HttpResponse(template.render())
def mysecond_views(request):
    template=loader.get_template('mysecond.html')
    return HttpResponse(template.render())
def shop_views(request):
    template=loader.get_template('shop.html')
    return HttpResponse(template.render())
def access_views(request):
    template=loader.get_template('accessory.html')
    return HttpResponse(template.render())
def lakme_views(request):
    template=loader.get_template('lakme.html')
    return HttpResponse(template.render())
def maybelline_views(request):
    template=loader.get_template('maybelline.html')
    return HttpResponse(template.render())
def dazler_views(request):
    template=loader.get_template('dazler.html')
    return HttpResponse(template.render())
def nyka_views(request):
    template=loader.get_template('nyka.html')
    return HttpResponse(template.render())