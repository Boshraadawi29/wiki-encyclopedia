from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import util
import markdown as md
from . import forms
import random
from django.urls import reverse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title): 
    content = util.get_entry(title)
    if content == None:
    	return render(request, "encyclopedia/pagenotfound.html")
    return render(request, "encyclopedia/entrypage.html", {
        "content": md.markdown(content),
        "title": title
   })

def search(request):
    #queryOrig = request.GET.get('q', '')
    query = request.GET.get('q', '')
    entries = util.list_entries()
    if query in entries: 
    	return HttpResponseRedirect(reverse('title', kwargs= {'title': query}))
    matches = [entry for entry in entries if query.lower() in entry.lower()] 	 
           
    return render(request, "encyclopedia/matches.html", {
    	"matches": matches
    })	

def new_enry(request):
    if request.method == "POST":
    	form = forms.MyForm(request.POST)
    	if not form.is_valid():
    	    print(form.errors)
    	else: 
    	    entry_title = form.cleaned_data['Title']
    	    content = form.cleaned_data['Content']
    	    util.save_entry(entry_title, content)
    	    return HttpResponseRedirect(reverse('title', kwargs={'title': entry_title}))
    
    else:
    	form = forms.MyForm()
    return render(request, "encyclopedia/createnewpage.html", {
    "form": form})
    
def random_page(request):
    page = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse('title', kwargs={'title': page}))


def edit_page(request, titlee): 
    content = util.get_entry(titlee)
    if request.method == "POST":
        new_content = request.POST.get("new_content")
        util.save_entry(titlee, new_content)
        return redirect("title", title=titlee)
    return render(request, "encyclopedia/editpage.html", {
        "content": content
    }
    )

def valid_entry(title):
    return title not in util.list_entries()


