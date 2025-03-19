from flask import Flask, request, jsonify
from tasks import get_stock_price


app = Flask(__name__)

@app.route('/stock_price', methods=['POST'])
def stock_price():
    data = request.get_json()
    stock_name = data.get('stock_name')
    
    if not stock_name:
        return jsonify({'error': 'Nome da ação é necessário'}), 400
    get_stock_price.delay(stock_name)
    return jsonify({'message': 'Requisição processada com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)