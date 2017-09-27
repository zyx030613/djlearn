# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from west.models import Character
#from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django import forms
class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)
    zhou = forms.CharField(max_length=200)
# Create your views here.
#def first_page(request):
    #return HttpResponse("<p>西餐</p>")
def staff(request):
    staff_list = Character.objects.all()
    #staff_str = map(str,staff_list)
    #return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")
#def templay(request):
    #context  ={'label':' '.join(staff_str)}
    #context['label']     =  staff_str
    return render(request, 'templay.html',{'staffs':staff_list})
def form(request):
    return render(request, 'form.html')

#def inverstigate(request):
    #rlt = request.GET['staff_text']
    #return HttpResponse(rlt)
def investigate(request):
    ctx ={}
    ctx.update(csrf(request))
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():

            submitted= form.cleaned_data['name']
            nnnn=form.cleaned_data['zhou']
            new_record = Character(name=submitted)
            sec_record =  Character(name = nnnn)
            new_record.save()
            sec_record.save()
    form = CharacterForm()

    all_records= Character.objects.all()
    ctx['staffs'] = all_records
    ctx['form'] = form
    return render(request, "investigate.html", ctx)