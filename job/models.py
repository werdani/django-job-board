from django.db import models

# Create your models here.
JOB_TYPE = (
    ('full time','full time'),
    ('part time','part time'),
)
class job(models.Model):
    title=models.CharField(max_length=100)
    jobtype=models.CharField(max_length=20,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
