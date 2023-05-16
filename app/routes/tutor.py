from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Tutor
from app.classes.forms import TutorForm, FindTutorForm
from flask_login import login_required
import datetime as dt


@app.route('/tutor/list', methods=['GET', 'POST'])
@app.route('/tutors', methods=['GET', 'POST'])
@login_required
def tutorList():
    tutors = Tutor.objects()
    form = FindTutorForm()

    if form.validate_on_submit():
        if form.className.data != "NA" and form.sport.data != "NA":
            tutors = Tutor.objects(className__icontains=form.className.data, sport=form.sport.data)
        elif form.className.data == "NA" and form.sport.data != "NA":
            tutors = Tutor.objects(sport = form.sport.data)
        elif form.className.data != "NA" and form.sport.data == "NA":
            tutors = Tutor.objects(className__icontains=form.className.data)
        elif form.className.data == "NA" and form.sport.data == "NA" :
            tutors = Tutor.objects()
    

    return render_template('tutors.html',tutors=tutors, form=form)


@app.route('/tutor/new', methods=['GET', 'POST'])
@login_required
def tutorNew():
    
    form = TutorForm()

    if form.validate_on_submit():

        print(form.className.data)
        newTutor = Tutor(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            className = form.className.data,
            xtraInfo = form.xtraInfo.data,
            author = current_user.id,
            sport = form.sport.data,
            # This sets the modifydate to the current datetime.
            modify_date = dt.datetime.utcnow
        )
        # This is a method that saves the data to the mongoDB database.
        newTutor.save()

        return redirect(url_for('tutor',tutorId=newTutor.id))

    return render_template('tutorform.html',form=form)

@app.route('/tutor/<tutorId>')
def tutor(tutorId):
    thisTutor = Tutor.objects.get(id=tutorId)
    return render_template('tutor.html',tutor=thisTutor)

@app.route('/tutor/delete/<tutorID>')
# Only run this route if the user is logged in.
@login_required
def tutorDelete(tutorID):
    # retrieve the blog to be deleted using the blogID
    deleteTutor = Tutor.objects.get(id=tutorID)
    # check to see if the user that is making this request is the author of the blog.
    # current_user is a variable provided by the 'flask_login' library.
    if current_user == deleteTutor.author:
        # delete the blog using the delete() method from Mongoengine
        deleteTutor.delete()
        # send a message to the user that the blog was deleted.
        flash('The Tutor was deleted.')
    else:
        # if the user is not the author tell them they were denied.
        flash("You can't delete a tutor you don't own.")
    # Retrieve all of the remaining blogs so that they can be listed.
    tutors = Tutor.objects()  
    # Send the user to the list of remaining blogs.
    return render_template('tutors.html', tutors=tutors)

@app.route('/tutor/edit/<tutorID>', methods=['GET', 'POST'])
@login_required
def tutorEdit(tutorID):
    editTutor = Tutor.objects.get(id=tutorID)
    # if the user that requested to edit this blog is not the author then deny them and
    # send them back to the blog. If True, this will exit the route completely and none
    # of the rest of the route will be run.
    if current_user != editTutor.author:
        flash("You can't edit a tutor post you don't own.")
        return redirect(url_for('tutor',tutorID=tutorID))
    # get the form object
    form = TutorForm()
    # If the user has submitted the form then update the blog.
    if form.validate_on_submit():
        # update() is mongoengine method for updating an existing document with new data.
        editTutor.update(
            className = form.className.data,
            xtraInfo = form.xtraInfo.data,
            sport = form.sport.data,
            modify_date = dt.datetime.utcnow,
        )
        # After updating the document, send the user to the updated blog using a redirect.
        return redirect(url_for('tutor',tutorID=tutorID))

    # if the form has NOT been submitted then take the data from the editBlog object
    # and place it in the form object so it will be displayed to the user on the template.
    form.className.data = editTutor.className
    form.xtraInfo.data = editTutor.xtraInfo
    form.sport.data = editTutor.sport


    # Send the user to the blog form that is now filled out with the current information
    # from the form.
    return render_template('tutorform.html',form=form)