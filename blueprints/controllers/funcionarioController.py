from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db, cursor

rFuncionarioC = Blueprint("rFuncionarioC", __name__, template_folder="../templatesBp")


@rFuncionarioC.route('/apiLoginFunc', methods=['POST'])
def ApiLoginFunc():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']

        query = "SELECT * FROM funcionarios WHERE login = %s AND senha = %s"
        values = (nome, senha)

        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            return render_template("telaFunc.html")
        else:
            return render_template('loginFunc.html', resposta="Usuário ou senha inválida")
        

@rFuncionarioC.route("/apiCadastrarFunc", methods= ["POST"])
def ApiCadastrarFunc():
    if request.method == "POST":
        cpf = request.form['cpf']
        nome = request.form['nome']
        login = request.form['login']
        senha = request.form['senha']

        query = "INSERT INTO funcionarios (cpf, nome, login, senha) VALUES (%s,%s,%s,%s)"
        values = (cpf, nome, login, senha)
        cursor.execute(query, values)
    return redirect(url_for('rFuncionarioView.TelaCadastroFuncionarios'))


@rFuncionarioC.route("/apiEditarFuncionario", methods= ["POST"])
def ApiEditarFuncionario():
    if request.method == "POST":
        cpf = request.form['cpf']
        nome = request.form['nome']
        login = request.form['login']
        senha = request.form['senha']
        query = "UPDATE funcionarios SET nome = %s, login = %s, senha = %s WHERE (ra = %s)"
        values = (nome, login, senha, cpf)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rFuncionarioView.TelaCadastroFuncionario'))

@rFuncionarioC.route("/apiDeletarFuncionario", methods= ["POST"])
def ApiDeletarFuncionario():
    if request.method == "POST":
        cpf = request.form['cpf']

        query = "DELETE FROM funcionarios WHERE (cpf = %s)"
        values = (cpf,)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rFuncionarioView.TelaCadastroFuncionario'))