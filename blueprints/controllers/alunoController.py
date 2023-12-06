from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db, cursor

rAlunoC = Blueprint("rAlunoC", __name__, template_folder="../templatesBp")

@rAlunoC.route('/apiLoginAluno', methods=['POST'])
def ApiLoginAluno():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']

        query = "SELECT * FROM alunosx WHERE login = %s AND senha = %s"
        values = (nome, senha)

        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            id = user[0]
            return redirect(url_for('rAlunoView.TelaAluno',id=id))
        else:
            return render_template('loginAluno.html', resposta="Usuário ou senha inválida")
        
@rAlunoC.route("/apiCadastrarAluno", methods= ["POST"])
def apiCadastrarAluno():
    if request.method == "POST":
        ra = request.form['ra']
        nome = request.form['nome']
        login = request.form['ra']
        senha = request.form['ra']

        query = "INSERT INTO alunosx (ra, nome, login, senha) VALUES (%s,%s,%s,%s)"
        values = (ra, nome, login, senha)
        cursor.execute(query, values)
        db.commit()

        cursor.fetchall()

    return redirect(url_for('rAlunoView.TelaCadastroAlunos'))


@rAlunoC.route("/apiEditarAluno", methods= ["POST"])
def ApiEditarAluno():
    if request.method == "POST":
        ra = request.form['ra']
        nome = request.form['nome']
        login = request.form['login']
        senha = request.form['senha']
        query = "UPDATE alunosx SET nome = %s, login = %s, senha = %s WHERE (ra = %s)"
        values = (nome, login, senha, ra)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rAlunoView.TelaCadastroAlunos'))


@rAlunoC.route("/apiDeletarAluno", methods= ["POST"])
def ApiDeletarAluno():
    if request.method == "POST":
        ra = request.form['ra']

        query = "DELETE FROM alunosx WHERE (ra = %s)"
        values = (ra,)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rAlunoView.TelaCadastroAlunos'))