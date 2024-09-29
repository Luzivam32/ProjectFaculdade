from flask import Blueprint


home_route = Blueprint('home_route', __name__)

@home_route.route('/')
def homepage():
    return "Sejam Bem-Vindo"

@home_route.route('/sobre')
def sobre_page():
    return "Esta é um pagina sobre nós"