from django.shortcuts import render

def home(request):
    return render(request, 'onlinecourse/course_details_bootstrap.html')

def submit(request, course_id):
    return render(request, 'onlinecourse/exam_result.html')

def show_exam_result(request, course_id):
    return render(request, 'onlinecourse/exam_result.html')