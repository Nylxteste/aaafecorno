from flask_restful import Resource, reqparse
jogadores = [{
    'nome': 'Gil',
    'senha': '22022001',
    'Score':0

},{
    'nome': 'Gabs',
    'senha': '22022001',
    'Score': 0

},{
    'nome': 'Rick',
    'senha': '22022001',
    'Score': 0

}]


class Jogadores(Resource):
    def get(self):
        lista_jogadores = []
        for jogador in jogadores:
            lista_jogadores.append({'Nome':jogador['nome'],
             'Score': jogador['Score']})

        return lista_jogadores,200

class VerificaJogador(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('senha')
    def get(self,nome_jogador,senha_jogador):
        count = 0
        for jogador in jogadores:
            count += 1
            if jogador['nome'] == nome_jogador and jogador['senha'] == senha_jogador:
                return {'message': 'Login aceito. Você será redirecionado em instantes...'}, 200
            if count >= len(jogadores):
                return {'message': 'Usuário não encontrado ou Senha incorreta.'},200

    def post(self,**kwargs):
        dados = VerificaJogador.argumentos.parse_args()
        for jogador in range(len(jogadores)-1, 0, -1):
            if dados['nome'] != jogadores[jogador]['nome'] or dados['senha'] != jogadores[jogador]['senha']:
                dados['Score'] = 0
                jogadores.append(dados)
                return jogadores
            else:
                return {'message': 'Usuário já cadastrado.'}

