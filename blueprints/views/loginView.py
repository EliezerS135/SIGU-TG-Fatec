from flask import Blueprint, render_template, redirect, request, url_for

rLoginView = Blueprint("rLoginView", __name__, template_folder="../templatesBp")


@rLoginView.route("/")
def principal():
    return render_template("home.html")

@rLoginView.route("/telaLoginAluno")
def TelaLoginAluno():
    return render_template("loginAluno.html")

@rLoginView.route("/telaLoginFunc")
def TelaLoginFunc():
    return render_template("loginFunc.html")

