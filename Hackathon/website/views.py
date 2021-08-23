from flask import Blueprint, render_template
from flask_login import current_user
views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html", user=current_user)


@views.route("/class-8")
def class_8():
    return render_template("class-8.html", user=current_user)


@views.route("/class-8/maths")
def maths():
    return render_template("maths.html", user=current_user)


@views.route("/class-8/maths/chapter-1")
def maths1():
    return render_template("chapter1.html", user=current_user)


@views.route("/class-8/maths/chapter-2")
def maths2():
    return render_template("chapter2.html", user=current_user)


@views.route("/class-8/maths/chapter-3")
def maths3():
    return render_template("chapter3.html", user=current_user)


@views.route("/class-8/maths/chapter-4")
def maths4():
    return render_template("chapter4.html", user=current_user)


@views.route("/class-8/maths/chapter-5")
def maths5():
    return render_template("chapter5.html", user=current_user)


@views.route("/class-8/maths/chapter-6")
def maths6():
    return render_template("chapter6.html", user=current_user)


@views.route("/class-8/maths/chapter-7")
def maths7():
    return render_template("chapter7.html", user=current_user)


@views.route("/class-8/maths/chapter-8")
def maths8():
    return render_template("chapter8.html", user=current_user)


@views.route("/class-8/maths/chapter-9")
def maths9():
    return render_template("chapter9.html", user=current_user)


@views.route("/class-8/maths/chapter-10")
def maths10():
    return render_template("chapter10.html", user=current_user)


@views.route("/class-8/maths/chapter-11")
def maths11():
    return render_template("chapter11.html", user=current_user)


@views.route("/class-8/maths/chapter-12")
def maths12():
    return render_template("chapter12.html", user=current_user)


@views.route("/class-8/maths/chapter-13")
def maths13():
    return render_template("chapter13.html", user=current_user)


@views.route("/class-8/maths/chapter-14")
def maths14():
    return render_template("chapter14.html", user=current_user)


@views.route("/class-8/maths/chapter-15")
def maths15():
    return render_template("chapter15.html", user=current_user)


@views.route("/class-8/maths/chapter-16")
def maths16():
    return render_template("chapter16.html", user=current_user)
