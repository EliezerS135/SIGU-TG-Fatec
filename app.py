from flask import Flask, render_template, request, redirect, url_for
from blueprints.views.loginView import rLoginView
from blueprints.views.alunoView import rAlunoView
from blueprints.views.funcionarioView import rFuncionarioView
from blueprints.views.disciplinaView import rDisciplinaView
from blueprints.views.notaView import rNotaView
from blueprints.controllers.alunoController import rAlunoC
from blueprints.controllers.disciplinaController import rDisciplinaC
from blueprints.controllers.funcionarioController import rFuncionarioC
from blueprints.controllers.notaController import rNotaC

app = Flask(__name__)

# Registro dos blueprints de views
app.register_blueprint(rLoginView)
app.register_blueprint(rAlunoView)
app.register_blueprint(rFuncionarioView)
app.register_blueprint(rDisciplinaView)
app.register_blueprint(rNotaView)

# Registro dos blueprints de controllers
app.register_blueprint(rAlunoC)
app.register_blueprint(rDisciplinaC)
app.register_blueprint(rFuncionarioC)
app.register_blueprint(rNotaC)


if __name__ == "__main__":
    app.run(debug=True)