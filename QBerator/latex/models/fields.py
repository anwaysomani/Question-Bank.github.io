"""
Models for admin field. Accesible to adminsitrator. By law_er_rule
Models engaged: Branch, Specialization, Semester, Subject, Module, Chapter

Developer: Anway Somani

"""

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from ..constant import SUBJECT_CATEGORY
from .question import SubjectCategory

# Model: Branch
class Branch(models.Model):
    branch = models.CharField(max_length=75)
    branch_abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.branch

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

# Model: Specialization
class Specialization(models.Model):
    branch = models.ForeignKey(Branch)
    primary_specialization = models.CharField(max_length=30)
    secondary_specialization = models.CharField(max_length=30, blank=True)
    specialization_abbreviation = models.CharField(max_length=20)

    def __str__(self):
        return self.branch.branch_abbreviation + " " + self.specialization_abbreviation

    class Meta:
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'

# Mdoel: Semester
class Semester(models.Model):
    specialization = models.ForeignKey(Specialization)
    semester = models.CharField(max_length=7)

    class Meta:
        unique_together = [("specialization", "semester")]

    def __str__(self):
        return self.specialization.branch.branch_abbreviation + " " + self.specialization.specialization_abbreviation + " - " + self.semester

    class Meta:
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'
    

# Model: Subject
class Subject(models.Model):
    semester = models.ManyToManyField(Semester)
    subject = models.CharField(max_length=75, unique=True)
    subject_code = models.CharField(max_length=6, null=True, blank=True)
    category = models.ForeignKey(SubjectCategory)
    module_type = models.CharField(max_length=2, null=True, blank=True)
    credits = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)], null=True, blank=True)

    def clean_module_type(self):
        return self.cleaned_data["module_type"].upper()

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.subject

    #class Meta:
    #    verbose_name = 'Subject'
    #    verbose_name_plural = 'Subjects'

# Model: Module
class Module(models.Model): 
    subject = models.ForeignKey(Subject)
    module = models.CharField(max_length=75)

    def __str__(self):
        return self.module

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

# Model: Chapter
class Chapter(models.Model):
    module = models.ForeignKey(Module)
    chapter = models.CharField(max_length=150)
    
    def __str__(self):
        return self.chapter

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'
