from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
job_title = [
    "First Job",
    "seconde Job",
    "third Job"
]

job_descripton = [
    "First job description",
     "second job description"
]
def hello(request):
    return HttpResponse("Hello World")

def job_detail(request, id):
    if id == 0:
        return redirect('/')
    return_html = f"h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)



def job_list(request):
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        list_of_jobs += f"<li><a href='job/{job_id}'>{j}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)
    

