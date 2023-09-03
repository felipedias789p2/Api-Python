from flask import Flask,jsonify,request


app = Flask(__name__)

carros = [

    {
        'id':1,
        'modelo':'Ford KA jk',
        'ano':   '1985'
    },
     {
        'id':2,
        'modelo':'Citroen C6',
        'ano':   '2016'
    },
    {
        'id':3,
        'modelo':'Fusca',
        'ano':   '1978'
    }
]

@app.route('/carros',methods =['GET'])
def obterCarros():
    return jsonify(carros)

@app.route('/carros/<int:id>',methods = ['GET'])
def obterPorId(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)
    return jsonify('{message: Nao existe este carro em nosso cadastro cadastro}')

@app.route('/carros/create',methods =['POST'])
def criarCadastroCarro():
    carro = request.get_json()
    carros.append(carro)
    return jsonify(carros)

@app.route('/carros/edit/<int:id>',methods =['PUT'])
def editarCadastroCarro(id):
    carroAltera = request.get_json()
    for indice,carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carroAltera)
            return jsonify(carros[indice])
    carros.append(carroAltera)
    return jsonify(carros)


app.run(port=5000, host= 'localhost',debug =True)