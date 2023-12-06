from flask import Blueprint, render_template, redirect, request, url_for
from blueprints.models import db, cursor

rNotaC = Blueprint("rNotaC", __name__, template_folder="../templatesBp")

@rNotaC.route("/apiCadastrarNota", methods= ["POST"])
def ApiCadastrarNota():
    if request.method == "POST":
        ra = request.form['ra']
        mat_id = request.form['mat_id']
        nota = request.form['nota']
        query = "INSERT INTO notas (ra, mat_id, nota) VALUES (%s, %s, %s)"
        values = (ra, mat_id, nota )
        cursor.execute(query, values)
    return redirect(url_for('rNotaView.TelaCadastroNota'))



@rNotaC.route("/apiEditarNota", methods= ["POST"])
def ApiEditarNota():
    if request.method == "POST":
        id = request.form['id']
        nota = request.form['nota']
        query = "UPDATE notas SET nota = %s WHERE (nota_id = %s)"
        values = (nota, id)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rNotaView.TelaCadastroNotas'))


@rNotaC.route("/apiDeletarNota", methods= ["POST"])
def ApiDeletarNota():
    if request.method == "POST":
        id = request.form['id']

        query = "DELETE FROM notas WHERE (nota_id = %s)"
        values = (id,)
        cursor.execute(query, values)
        db.commit()
        cursor.fetchall()

    return redirect(url_for('rNotaView.TelaCadastroNota'))
