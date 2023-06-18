from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=500)
  img_src = models.CharField(max_length=700)
  short_description = models.CharField(max_length=500)
  show_in_landing = models.BooleanField(null=False, default=False)
  content = models.TextField()


  def __str__(self) -> str:
    return self.title


class Job(models.Model):
  date_start = models.DateField(null=False)
  date_end = models.DateField(default=None, blank=True, null=True)
  active = models.BooleanField(null=False, default=False)
  company_name = models.CharField(max_length=500, null=False)
  position_name = models.CharField(max_length=500, null=False)
  description = models.TextField(null=False)

  
  def __str__(self) -> str:
    return f'{self.company_name} - {self.position_name}'
