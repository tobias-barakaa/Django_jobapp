from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader

class TempClass:
    x = 5

# Create your views here.
job_title = [
    "First Job",
    "seconde Job",
    "third Job"
]

job_descripton = [
    "First job description",
     "second job description",
     "third job description"
]
def hello(request):
    return HttpResponse("Hello World")

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('job_home'))
        return_html = f"h1>{job_title[id]}</h1> <h3>{job_descripton[id]}</h3>"
        return HttpResponse(return_html)
    except:
        return HttpResponse("Invalid Job Id")



def job_list(request):
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        list_of_jobs += f"<li><a href='job/{job_id}'>{j}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)

def hello(request):
    # is_authenticated = False
    # list = ["alpha", "beta"]
    # temp = TempClass()
    # context ={"name": "John Doe", "age": 10, "first_list":
    #     list, "temp_object": temp, "is_authenticated": is_authenticated}
    # return render(request, "app/job_list.html", context)
    context={"job_title_list": job_title}
    return render(request, "app/job_list.html", context)
    
    
def job_detail(request, id):
    print(type(id))
    try:
        if id == 0:
            return redirect(reverse('job_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_descripton[id]}</h3>"
        # return HttpResponse(return_html)
        context ={"job_title": job_title[id], "job_description": job_descripton[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponse("Invalid Job Id")

