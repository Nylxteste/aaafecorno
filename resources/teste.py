

jogadores = [{
            'nome': 'Gil',
            'senha': '22022001',
            'Score': 10

        },{
            'nome': 'Geil',
            'senha': '22022001',
            'Score': 10

        }]

valor = { 'nome': 'Geil',
         'senha': '22022001',
         'Score': 10}

for jogador in jogadores:
    if valor['nome'] == jogador['nome'] and valor['senha'] == jogador['senha']:
        print('mensagem', 'seu cafchorro')
