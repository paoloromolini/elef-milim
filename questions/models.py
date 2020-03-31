from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    lesson_link = models.URLField(blank=True, null=True)
    audio_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug


class Question(models.Model):
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField()
    correct_answers = models.CharField(max_length=250, help_text="List separated by comma")
    css_class = models.CharField(max_length=250, blank=True, null=True)
    position = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)

    def __str__(self):
        return self.text

    @property
    def correct_answers_list(self):
        print(self.correct_answers.split(','))
        return self.correct_answers.split(',')
