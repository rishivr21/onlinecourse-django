from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # create submission
    submission = Submission.objects.create()

    # get selected answers
    choices = request.POST.getlist('choice')

    for choice_id in choices:
        choice = Choice.objects.get(pk=int(choice_id))
        submission.choice_set.add(choice)

    submission.save()

    # redirect to exam result page
    return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):

    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    total_score = 0
    possible_score = 0

    questions = Question.objects.filter(lesson__course=course)

    for question in questions:
        possible_score += question.grade

        selected_choices = submission.choice_set.filter(question=question)

        if question.is_get_score(selected_choices):
            total_score += question.grade

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)