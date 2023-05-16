# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, SelectMultipleField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role', choices=[('Student Athletes', 'Student Athletes'), ('Parents', 'Parents')])
    grade = SelectField('Grade Year', choices=[(9, 9), (10, 10), (11, 11), (12, 12)])

class BlogForm(FlaskForm):
    sport = SelectField('Sport', choices=[('Soccer', 'Soccer'), ('Baseball', 'Baseball'), ('Volleyball', 'Volleyball'), ('Basketball', 'Basketball'), ('Swimming', 'Swimming'), ('Running', 'Running'), ('Other', 'Other')])
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class TutorForm(FlaskForm):
    sport = SelectField('Sport', choices=[('Soccer', 'Soccer'), ('Baseball', 'Baseball'), ('Volleyball', 'Volleyball'), ('Basketball', 'Basketball'), ('Swimming', 'Swimming'), ('Running', 'Running'), ('Football', 'Football'), ('Other', 'Other')])
    className = SelectMultipleField('Classes You Want to Tutor:', choices=[('Algebra 1', 'Algebra 1'), ('Geometry', "Geometry"), ('Algebra 2', 'Algebra 2'), ('Pre-calc', 'Pre-calc'), ('Calc AB', 'Calc AB'), ('Calc BC', 'Calc BC'), ('Statistics', 'Statistics'), ('AP Stats', 'AP Stats'), ('Bio', 'Bio'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Physiology', 'Physiology'), ('APES', 'APES'), ('AP Physics', 'AP Physics'), ('AP Bio', 'AP Bio'), ('APCSP', 'APCSP'), ('APCSA', 'APCSA'), ('Sentence Diagrams', 'Sentence Diagrams'), ('Essay Editing', 'Essay Editing'), ('AP Lit', 'AP Lit'), ('Ethnic Studies', 'Ethnic Studies'), ('World History', 'World History'), ('US History', 'US History'), ('US Gov', 'US Gov'), ('Comp Gov', 'Comp Gov')])
    xtraInfo = TextAreaField('Extra Info:', validators=[DataRequired()])
    submit = SubmitField('Post')

class FindTutorForm(FlaskForm):
    sport = SelectField('Sport of choice: ', choices=[('Soccer', 'Soccer'), ('Baseball', 'Baseball'), ('Volleyball', 'Volleyball'), ('Basketball', 'Basketball'), ('Swimming', 'Swimming'), ('Running', 'Running'), ('Football', 'Football'), ('Other', 'Other'), ('NA', 'No preference')])
    className = SelectField('Classes you need help with: ', choices=[('Algebra 1', 'Algebra 1'), ('Geometry', "Geometry"), ('Algebra 2', 'Algebra 2'), ('Pre-calc', 'Pre-calc'), ('Calc AB', 'Calc AB'), ('Calc BC', 'Calc BC'), ('Statistics', 'Statistics'), ('AP Stats', 'AP Stats'), ('Bio', 'Bio'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Physiology', 'Physiology'), ('APES', 'APES'), ('AP Physics', 'AP Physics'), ('AP Bio', 'AP Bio'), ('APCSP', 'APCSP'), ('APCSA', 'APCSA'), ('Sentence Diagrams', 'Sentence Diagrams'), ('Essay Editing', 'Essay Editing'), ('AP Lit', 'AP Lit'), ('Ethnic Studies', 'Ethnic Studies'), ('World History', 'World History'), ('US History', 'US History'), ('US Gov', 'US Gov'), ('Comp Gov', 'Comp Gov'), ('NA', 'No preference')])
    submit = SubmitField('Filter')
