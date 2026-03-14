from django.db import models

# Course model
class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Question model
class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


# Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.choice_text


# Submission model
class Submission(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    choices = models.ManyToManyField(Choice)