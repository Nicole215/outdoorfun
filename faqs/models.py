from django.db import models


class FAQ(models.Model):
    """ FAQs to answer to most asked question users might have """
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class ContactRequest(models.Model):
    """ Contact Form for User to contact site admin """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact request from {self.name}"
