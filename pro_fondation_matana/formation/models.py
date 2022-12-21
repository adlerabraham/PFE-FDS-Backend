from django.db import models
from django.template.defaultfilters import slugify
from school.models import *
from pro_fondation_matana.mixins import *


# Create your models here.


class Program(AuditMixin, SoftDeleteModel, models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    Institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='institution')
    logo=models.ImageField(upload_to='program', blank=True)
    description = models.TextField(max_length = 100)
    responsible = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs) 

    class Meta :
        db_table = 'program'




class Period(AuditMixin, SoftDeleteModel, models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    start_date = models.DateField(max_length=25, blank=False, null=True)
    end_date = models.DateField(max_length=25, blank=False, null=True)
    coefficient = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs) 

    
    class Meta :
        db_table = 'period'
    



class Program_period(AuditMixin, SoftDeleteModel, models.Model):

    class Unit_duration (models.TextChoices):
        mois = "month"
        annee = "year"
        
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField()
    unit_duration = models.CharField(max_length=25, choices=Unit_duration.choices, blank=False, null=True)
    number_student = models.IntegerField()
    number_teacher = models.IntegerField()


    
    class Meta :
        db_table = 'program_period'



class Level(AuditMixin, SoftDeleteModel, models.Model):
    level=models.SmallIntegerField()

    
    class Meta :
        db_table = 'level'



class Program_period_level(AuditMixin, SoftDeleteModel, models.Model):    
    program_period = models.ForeignKey(Program_period, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    
    class Meta :
        db_table = 'program_period_level'



class Classroom(AuditMixin, SoftDeleteModel, models.Model):
    program_period_level = models.ForeignKey(Program_period_level, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    abbreviation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs) 
    

    class Meta :
        db_table = 'classroom'




class Subject(AuditMixin, SoftDeleteModel, models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=500)

     
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs) 


    class Meta :
        db_table = 'subject'




class Subject_program_period(AuditMixin, SoftDeleteModel, models.Model):
    Programme_periode = models.ForeignKey(Program_period, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    

    class Meta :
        db_table = 'subject_program_period'




class Course(AuditMixin, SoftDeleteModel, models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    classe = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    coefficient = models.PositiveSmallIntegerField()
    logo=models.ImageField(upload_to='course', blank=True)
    #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

       
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs) 


    class Meta :
        db_table = 'course'




class Lesson(AuditMixin, SoftDeleteModel, models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    chapter = models.IntegerField()
    description = models.CharField(max_length=100)
    


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super().save(*args, **kwargs) 


    class Meta :
        db_table = 'lesson'