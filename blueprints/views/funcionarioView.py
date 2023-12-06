from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db

rFuncionarioView = Blueprint("rFuncionarioView", __name__, template_folder="../templatesBp")


@rFuncionarioView.route("/telaFunc")
def TelaFunc():
    return render_template("telaFunc.html")

@rFuncionarioView.route("/telaCadastroFuncionarios")
def TelaCadastroFuncionarios(): 
    mycursor = db.cursor()
    mycursor.execute('SELECT * FROM funcionarios')
    aluno = mycursor.fetchall()
    return render_template('funcionario_cadastro.html', dadosFuncionario=aluno)

@rFuncionarioView.route("/telaCadastrarFuncionario")
def TelaCadastrarFuncionario():
    return render_template("funcionarioCadastrar.html")

@rFuncionarioView.route("/telaFuncionarioEditar")
def TelaFuncionarioEditar():
    return render_template("funcionarioEditar.html")

@rFuncionarioView.route("/telaDeletarFuncionario")
def TelaDeletarFuncionario():
    return render_template("funcionarioDeletar.html")