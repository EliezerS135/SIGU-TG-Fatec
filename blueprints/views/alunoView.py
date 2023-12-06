from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db

rAlunoView = Blueprint("rAlunoView", __name__, template_folder="../templatesBp")


@rAlunoView.route("/telaAluno/<int:id>")
def TelaAluno(id):
    mycursor = db.cursor()
    mycursor.execute('SELECT mat_nome, nota FROM notas JOIN materias ON notas.mat_id = materias.mat_id WHERE ra = %s;', (id,))
    aluno = mycursor.fetchall()

    mycursor = db.cursor()
    mycursor.execute('SELECT nome,ra FROM alunosx WHERE ra = %s;', (id,))
    nomes = mycursor.fetchone()

    return render_template('telaAluno.html', dadosAluno=aluno, nome=nomes)

@rAlunoView.route("/telaCadastrarAluno")

def TelaCadastrarAluno():
    return render_template("alunoCadastrar.html")

@rAlunoView.route("/telaCadastroAlunos")
def TelaCadastroAlunos():
    mycursor = db.cursor()
    mycursor.execute('SELECT * FROM alunosx')
    aluno = mycursor.fetchall()
    return render_template('aluno_cadastro.html', dadosAluno=aluno)

@rAlunoView.route("/telaAlunoEditar")
def TelaAlunoEditar():
    return render_template("alunoEditar.html")


@rAlunoView.route("/telaDeletarAluno")
def TelaDeletarAluno():
    return render_template("alunoDeletar.html")