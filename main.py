from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.jogador import Jogadores, VerificaJogador


app = Flask(__name__)
api = Api(app)

CORS(app, supports_credentials=True)

api.add_resource(Jogadores, '/jogadores')
api.add_resource(VerificaJogador, '/jogadores/nome=<string:nome_jogador>&senha=<string:senha_jogador>')

if __name__ == '__main__':
    app.run(debug=True)