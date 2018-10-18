from django.contrib import admin
from .models import *

# Combining Modules:
# ------------------

# Module View
"""
class ModuleTabularInline(admin.TabularInline):
    model = Modules
    min_length = 2

# Inserting Module in Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleTabularInline]
    
    class Meta:
        model = Course

# Inserting List Display Views
class branchdisp(admin.ModelAdmin):
    list_display = ('branch', 'specialization'),

class semesterdisp(admin.ModelAdmin):
    list_display = ('branch', 'sem_abbreviation'),

#class coursedisp(admin.ModelAdmin):
 #   list_display = ('sem_abbreviation', 'course', 'course_code')

class moduledisp(admin.ModelAdmin):
    list_display = ('course', 'module')
"""

admin.site.register(Question)
admin.site.register(Branch)
admin.site.register(Specialization)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Module)
admin.site.register(Chapter)

# My Declare Field
admin.site.register(DeclareSemester)