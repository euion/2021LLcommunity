from django.db import models
from account.models import Profile

# Create your models here.

class Crud(models.Model):
    title = models.CharField(max_length=200)
    profile_id = models.ForeignKey(Profile, related_name="Crud_profile", on_delete=models.CASCADE, db_column="Crud_profile_id")
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    #image = models.ImageField(upload_to="media/freeImages/")

    def __str__(self):
        return self.title

# Crud의 댓글 모델
class CrudComment(models.Model):
    crud_id = models.ForeignKey(Crud, related_name="crud", on_delete=models.CASCADE, db_column="crud_id")
    profile_id = models.ForeignKey(Profile, related_name="CrudComment_profile", on_delete=models.CASCADE, db_column="CrudComment_profile_id")
    pub_date = models.DateTimeField('date published')
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name + " - " + str(self.pub_date)


class Info(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50 , null=True )
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

# Info의 댓글 모델
class InfoComment(models.Model):
    info_id = models.ForeignKey(Info, related_name="info", on_delete=models.CASCADE, db_column="info_id")
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name + " - " + str(self.pub_date)


class Qna(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50 , null=True)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title

# Qna의 댓글 모델
class QnaComment(models.Model):
    qna_id = models.ForeignKey(Qna, related_name="qna", on_delete=models.CASCADE, db_column="qna_id")
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name + " - " + str(self.pub_date)