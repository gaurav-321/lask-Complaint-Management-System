from app import app, db, allowed_file
from flask import url_for, redirect, render_template, request, jsonify, session, flash
from models import User, Complaint, Department
from methods import login_user, user_logged
from form import LoginForm, RegistrationForm, ComplaintForm
from werkzeug.utils import secure_filename
import os


@app.route('/')
def home_page():
    return render_template("index.html", current=110)


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if "logged_in" in session.keys() and session['logged_in'] is True:
        return redirect("/")
    else:
        if request.method == "POST":
            data = request.form.to_dict()
            user = User.query.filter_by(username=data['username'], password=data['password']).first()
            if user:
                login_user(data, user.role)
                flash(f'User has been successfully registered', 'success')
                return redirect("/")
            else:
                flash(f'Incorrect User/Password', 'danger')
                return redirect("/login")
        else:
            return render_template("login.html", form=form)


@app.route("/register", methods=['POST', 'GET'])
def register_page():
    form = RegistrationForm()
    if request.method == "POST":
        print(request.environ['HTTP_ORIGIN'])
        data = request.form.to_dict()
        if User.query.filter_by(username=data['username']).first():
            flash("User is already registered", "danger")
            return redirect("/register") if data['type'] == "visitor" else redirect("/admin?id=3")
        user = User(data['username'], data['password'], data['type'])
        db.session.add(user)
        db.session.commit()
        flash(f'User has been successfully registered', 'success')
        return redirect("/login") if data['type'] == "visitor" else redirect("/admin?id=3")

    else:
        return render_template("/register.html", form=form)


@app.route("/send_complaint", methods=['POST', 'GET'])
def send_complaint():
    if user_logged() or 1 == 1:
        form = ComplaintForm()
        if request.method == "POST":
            if True is True:
                data = request.form.to_dict()
                files = request.files.getlist('media[]')
                filenames = []
                for file in files:
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        filenames.append(filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                complaint_query = Complaint(data['title'], data['description'], data['location'], ",".join(filenames))
                db.session.add(complaint_query)
                db.session.commit()
                flash('File(s) successfully uploaded')
                return redirect('/complaint')
            else:
                flash("Please Complete Form", "danger")
                return redirect("/send_complaint")

        else:
            return render_template("send_complaint.html", form=form)
    else:
        return redirect("/unauthorized")


@app.route("/complaint", methods=['GET'])
def complaint():
    complaints = get_complaints()
    if request.args.get("show") is "resolved":
        return render_template("complaint.html", complaints=[x for x in complaints if x.status == "resolved"])
    else:
        return render_template("complaint.html", complaints=complaints)


@app.route("/admin", methods=['GET', 'POST'])
def admin_page():
    form = RegistrationForm()
    if request.method == "POST":
        data = request.form.to_dict()
        if "dept" in data.keys():
            department = Department(data['dept'])
            db.session.add(department)
            db.session.commit()
            return redirect(f"/admin?id=2")
        else:
            obj = Complaint.query.filter_by(id=data['complaint_id']).one()
            obj.assign = data['dept_name']
            db.session.commit()
            return redirect(f"/admin?id=1")
    elif request.args.get("delete"):
        obj = Department.query.filter_by(id=int(request.args.get("delete"))).one()
        db.session.delete(obj)
        db.session.commit()
        return redirect(f"/admin?id=2")
    elif request.args.get("del_comp"):
        obj = Complaint.query.filter_by(id=int(request.args.get("del_comp"))).one()
        db.session.delete(obj)
        db.session.commit()
        return redirect(f"/admin?id=1")
    else:
        return render_template("admin.html", page=request.args.get("id"), departments=get_department(), form=form,
                               complaints=[x for x in get_complaints()])


@app.route("/faculty")
def faculty():
    if request.args.get("delete"):
        obj = Complaint.query.filter_by(id=int(request.args.get("delete"))).one()
        db.session.delete(obj)
        db.session.commit()
        return redirect(f"/faculty")
    elif request.args.get("completed"):
        obj = Complaint.query.filter_by(id=int(request.args.get("completed"))).one()
        obj.status = "resolved"
        db.session.commit()
        return redirect(f"/faculty")
    return render_template("faculty.html", complaints=[x for x in get_complaints() if
                                                       x[-1] == session['dept'] and x[-2] == "new"])


@app.route("/logout")
def logout():
    del session['logged_in']
    del session['username']
    del session['password']
    return redirect("/login")


@app.route("/unauthorized")
def unauthorized():
    return "unauthorized user"


@app.route('/uploads/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


def get_complaints():
    complaints = Complaint.query.order_by(Complaint.id).all()
    return [(x.id, x.title, x.description, x.location, x.media, x.status, x.assign) for x in complaints]


def get_department():
    department = Department.query.order_by(Department.id).all()
    return [(x.id, x.name) for x in department]


# db.session.query(Complaint).delete()
# db.session.commit()
db.create_all()
