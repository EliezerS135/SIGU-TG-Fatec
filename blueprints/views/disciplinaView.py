from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db

rDisciplinaView = Blueprint("rDisciplinaView", __name__, template_folder="../templatesBp")

@rDisciplinaView.route("/telaCadastroDis")
def TelaCadastroDis(): 
    mycursor = db.cursor()
    mycursor.execute('SELECT * FROM materias')
    aluno = mycursor.fetchall()
    return render_template('disciplina_cadastro.html', dados=aluno)

@rDisciplinaView.route("/telaCadastrarDis")
def TelaCadastrarDis():
    return render_template("disciplinaCadastrar.html")

@rDisciplinaView.route("/telaDisEditar")
def TelaDisEditar():
    return render_template("disciplinaEditar.html")

@rDisciplinaView.route("/telaDeletarDis")
def telaDeletarDis():
    return render_template("disciplinaDeletar.html")