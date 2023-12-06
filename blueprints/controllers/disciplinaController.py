from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db, cursor

rDisciplinaC = Blueprint("rDisciplinaC",  __name__, template_folder="../templatesBp")

@rDisciplinaC.route("/apiCadastrarDis", methods= ["POST"])
def ApiCadastrarDis():
    if request.method == "POST":
        nome = request.form['nome']
        query = "INSERT INTO materias (mat_nome) VALUES (%s)"
        values = (nome, )
        cursor.execute(query, values)
    return redirect(url_for('rDisciplinaView.TelaCadastroDis'))


@rDisciplinaC.route("/apiEditarDis", methods= ["POST"])
def apiEditarDis():
    if request.method == "POST":
        id = request.form['id']
        nome = request.form['nome']
        query = "UPDATE materias SET mat_nome = %s WHERE (mat_id = %s)"
        values = (nome, id)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rDisciplinaView.TelaCadastroDis'))



@rDisciplinaC.route("/apiDeletarDis", methods= ["POST"])
def ApiDeletarDis():
    if request.method == "POST":
        id = request.form['id']

        query = "DELETE FROM materias WHERE (mat_id = %s)"
        values = (id,)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rDisciplinaView.TelaCadastroDis'))