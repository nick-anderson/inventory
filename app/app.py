from typing import List, Dict
from flask import Flask, abort, jsonify, render_template, request
import mysql.connector
import json
import sys
from decimal import Decimal
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


# app = Fla sk(__name__)

@app.route('/inventory', methods=['POST','GET'])
def inventory():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'interview'
    }
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        productID = data['productID'][0]
        availableQuantity = data['availableQuantity'][0]
        cursor.execute('INSERT INTO inventory (productID,availableQuantity) VALUES(%s, %s)', (str(productID), str(availableQuantity)))
        connection.commit()
        cursor.close()
        return jsonify({
            'status': 'Query Succesful!',
            'productID': productID,
            'availableQuantity': availableQuantity
        })

    if request.method == 'GET':
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('''
        SELECT m1.productId,m1.availableQuantity
        FROM inventory m1 LEFT JOIN inventory m2
        ON (m1.productID = m2.productID AND m1.record < m2.record)
        WHERE m2.productID IS NULL;
        ''')
        num_products = cursor.fetchall()
        allData = []
        print(num_products)
        for i in range(len(num_products)):
            productID = num_products[i][0]
            availableQuantity = num_products[i][1]
            dataDict = {
                "productID": productID,
                "availableQuantity": availableQuantity
            }
            allData.append(dataDict)

        return jsonify(allData)



@app.route('/product', methods=['POST', 'GET'])
def product():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'interview'
    }
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        id = data['id'][0]
        name = data['name'][0]
        image = data['image'][0]
        price = data['price'][0]
        cursor.execute('INSERT INTO product (id,name,image,price) VALUES(%s, %s, %s, %s)', (str(id),str(name), str(image),str(price)))
        connection.commit()
        cursor.close()
        return jsonify({
            'status': 'Query Succesful!',
            'id': id,
            'name': name,
            'image': image,
            'price': price
        })


@app.route('/orders', methods=['POST'])
def order():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'interview'
    }
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        id = data['id'][0]
        productID = data['productID'][0]
        quantity = data['quantity'][0]
        price = data['price'][0]
        cursor.execute('INSERT INTO orders (id,productID,quantity,price) VALUES(%s, %s, %s, %s)', (str(id),str(productID), str(quantity),str(price)))
        # cursor.execute('INSERT INTO orders (id,productID,quantity,price) VALUES(123,12345,50,90)', (str(id),str(productID), str(quantity),str(price)))
        # val = cursor.execute('SELECT availableQuantity from inventory WHERE productID LIKE 2')
        # print('This is standard output',val, file=sys.stdout)
        connection.commit()
        cursor.close()
        return jsonify({
            'status': 'Query Succesful!',
            'productID': productID,
            'id': id,
            'quantity': quantity,
            'price': price
        })



#
def top_sales() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'interview'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    # print('This is standard output', file=sys.stdout)
    query ='''
    select productID, sum(quantity) as total_sales from orders group by productID order by SUM(quantity) DESC LIMIT 5;
    '''
    cursor.execute(query)
    results = [{productID: str(total_sales)} for (productID, total_sales ) in cursor]
    cursor.close()
    connection.close()
    return results
#
# @app.route('/sales')
# def top() -> str:
#     return json.dumps({'top_sales': top_sales()})
# #

@app.route('/sales/<items>/')
def sales(items):
    """Example endpoint returning a list of top sales
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: empty
        type: string
        enum: ['all']
        required: false
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/sales'
      Sales:
        type: string
    responses:
      200:
        description: Return JSON of top sales
        schema:
    """
    return json.dumps({'top_sales': top_sales()})



# def alert_func() -> List[Dict]:
#     config = {
#         'user': 'root',
#         'password': 'root',
#         'host': 'db',
#         'port': '3306',
#         'database': 'interview'
#     }
#     connection = mysql.connector.connect(**config)
#     cursor = connection.cursor()
#     # print('This is standard output', file=sys.stdout)
#     query ='''
#     select DISTINCT(productID) as low_product from inventory WHERE availableQuantity < 5;
#     '''
#     cursor.execute(query)
#     results = [{low_product: str(low_product)}]
#     cursor.close()
#     connection.close()
#     return results

@app.route('/alert', methods=['POS  T','GET'])
def alert():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'interview'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('''
    select DISTINCT(productID),availableQuantity as low_product from inventory WHERE availableQuantity < 5;
    ''')
    num_products = cursor.fetchall()
    allData = []
    # print(num_products)
    for i in range(len(num_products)):
        productID = num_products[i][0]
        availableQuantity = num_products[i][1]
        dataDict = {
            "productID": productID,
            "availableQuantity": availableQuantity
        }
        allData.append(dataDict)

    return jsonify(allData)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
