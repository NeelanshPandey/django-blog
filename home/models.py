from django.db import models

# Create your models here.

class Blogs(models.Model):
    blogTitle=models.CharField(max_length=255)
    blogAuthor = models.CharField(max_length=122)
    blogContent=models.TextField()
    time=models.DateField()


class CommentBlog(models.Model):
    commentName = models.CharField(max_length=20)
    commentText = models.TextField()
    blog = models.ForeignKey('Blogs', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by Name: {self.commentName}"

class HelpMessage(models.Model):
    helpName=models.CharField(max_length=20)
    helpText=models.TextField()
    def __str__(self):
        return self.helpName
