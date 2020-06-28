from typing import List, Dict
from flask import Flask, abort, jsonify, render_template, request
import mysql.connector
import json
import sys
from decimal import Decimal


app = Flask(__name__)


@app.route('/inventory', methods=['POST', 'GET'])
def data():
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

@app.route('/sales')
def top() -> str:
    return json.dumps({'top_sales': top_sales()})
#

#
# @app.route('/top', methods=['POST', 'GET'])
# def top():
#     if request.method == 'GET':
#         config = {
#             'user': 'root',
#             'password': 'root',
#             'host': 'db',
#             'port': '3306',
#             'database': 'interview'
#         }
#         connection = mysql.connector.connect(**config)
#         cursor = connection.cursor()
#         query ='''
#         select productID, sum(quantity) as total_sales  from orderT group by productID order by SUM(quantity) DESC LIMIT 5;
#         '''
#
#         cursor.execute(query)
#         # 'select productID, sum(quantity) as total_sales  from orderT group by productID order by SUM(quantity) DESC LIMIT 5;
# # ')
#         # num_products = cursor.fetchall()
#         allData = []
#         print(num_products)
#         results = [{productID: total_sales} for (productID, total_sales) in cursor]
#         cursor.close()
#         connection.close()
#
#         return results
#
#         # for i in range(len(num_products)):
#         #     productID = num_products[i][0]
#         #     total_sales = num_products[i][1]
#         #     dataDict = {
#         #         "productID": productID,
#         #         "total_sales": total_sales
#         #     }
#         #     allData.append(dataDict)
#         #
#         # return jsonify(allData)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'interview'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM inventory')
    results = [{productID: availabbleQuantity} for (productID, availabbleQuantity) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})

#
#
#
# @app.route('/d')
# def index() -> str:
#     # return "ok4"
#     config = {
#         'user': 'root',
#         'password': 'root',
#         'host': 'db',
#         'port': '3306',
#         'database': 'interview'
#     }
#     connection = mysql.connector.connect(**config)
#     cursor = connection.cursor()
#     # cursor.execute('SHOW DATABASES;')
#     cursor.execute('SELECT * FROM product')
#     # results = [{name: color} for (name, color) in cursor]
#     cursor.close()
#     connection.close()
#     return "worked"
#
#
#     # return json.dumps({'favorite_colors': favorite_colors()})
#

if __name__ == '__main__':
    app.run(host='0.0.0.0')
