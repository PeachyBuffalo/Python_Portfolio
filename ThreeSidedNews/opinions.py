from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    viewpoint = models.CharField(max_length=100)  # e.g., "For", "Against"

class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    # Add more fields as needed

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    # Add user and other fields as needed