# views.py

# Importing from login.py
# -----------------------
# Main page, Faculty and HOD Login Page
#from .login import  main, faculty_login, hod_login
# Importing post-Login page
from .login import findex, hindex

# Improting class from login.py
#from .login import PanelRedirectView

# Importing error page
from .login import error

# Importing from facsem.py(faculty semester views)
from .facsem import sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8

# Improting from eachcrs.py(file containing question for each subject)
from .eachcrs import *

# Importing view from .epdf for Exporting file to pdf(trial)
from .epdf import html_to_pdf_view


