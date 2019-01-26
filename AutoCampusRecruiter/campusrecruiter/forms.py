from django import forms
from .models import Recruitment
from .models import Students

class AddForm(forms.Form):

   class Meta:
      model = Recruitment
      fields = ('col_name', 'col_address',)


class AddStudents(forms.Form):
    class Meta:
        model=Students
        fields = ('student_name', 'student_coll','roll_no','student_gpa')