from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db

rNotaView = Blueprint("rNotaView", __name__, template_folder="../templatesBp")

@rNotaView.route("/telaCadastroNotas")
def TelaCadastroNotas(): 
    mycursor = db.cursor()
    mycursor.execute('SELECT alunosx.ra, alunosx.nome, materias.mat_nome, notas.nota FROM notas JOIN materias ON notas.mat_id = materias.mat_id JOIN alunosx ON alunosx.ra = notas.ra ORDER BY alunosx.nome;')
    aluno = mycursor.fetchall()
    return render_template('notas_cadastro.html', dadosFuncionario=aluno)

@rNotaView.route("/telaCadastrarNota")
def TelaCadastrarNota():
    return render_template("notaCadastrar.html")

@rNotaView.route("/telaNotaEditar")
def telaNotaEditar():
    return render_template("notaEditar.html")

@rNotaView.route("/telaDeletarNota")
def TelaDeletarNota():
    return render_template("notaDeletar.html")