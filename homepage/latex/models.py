from django.db import models



class CreateQuestion(models.Model):
    BRANCH_CHOICE = (
            ('Bachelor Of Technology(B.Tech)', 'Bachelor Of Technology(B.Tech)'),
            ('Bachelor Of Computer Applications(BCA)', 'Bachelor Of Computer Applications(BCA)',),
            ('Bachelor Of Science(B.Sc)', 'Bachelor Of Science(B.Sc)'),
            ('Bachelor of Buisness Administration(BBA)', 'Bachelor Of Buisness Administration(BBA)'),
            ('Bachelor Of Commerce(B.Com)', 'Bachelor Of Commerce(B.Com)'),
    )
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICE)
    specialization = models.CharField(max_length=50)
    SEMESTER_CHOICE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
    )
    semester = models.IntegerField(choices=SEMESTER_CHOICE)
    course = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    chapter = models.CharField(max_length=40)
    question = models.CharField(max_length=250)
    MARK_CHOICE = (
            ('2', '2'),
            ('5', '5'),
            ('10', '10'),
    )
    marks = models.IntegerField(choices=MARK_CHOICE)
    PRIORITY_CHOICE = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
    )
    priority = models.IntegerField(choices=PRIORITY_CHOICE)
    notes = models.CharField(max_length=200)
    
