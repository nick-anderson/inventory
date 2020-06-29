import os

#Create latest quantity for product1
print('Register new product information to products DB')
print('')
register_product = '''
curl --location --request POST "localhost:5000/product" \
--form "id=99" \
--form "name=tomatoes" \
--form "image=http://tomatoes.com" \
--form "price=2" '''
os.system(register_product)
print('')

#Create latest quantity for product1
print('Updating availableQuantity for productID1 to DB')
print('')
update_quantity_1 = '''
curl --location --request POST "localhost:5000/inventory" \
--form "availableQuantity=55" \
--form "productID=1" '''
os.system(update_quantity_1)
print('')

#Create latest quantity for product2
print('Updating availableQuantity for productID2 to DB')
print('')
update_quantity_2 = '''
curl --location --request POST "localhost:5000/inventory" \
--form "availableQuantity=300" \
--form "productID=2" '''
os.system(update_quantity_2)
print('')

#New Order comes in of a purchase of 50
print('New order of 50 comes in for tomatoes, insert of order quantity of Product2 to DB')
print('')
order_update_1 = '''
curl --location --request POST "localhost:5000/orders" \
--form "id=99" \
--form "productID=2" \
--form "quantity=50" \
--form "price=95"
'''
os.system(order_update_1)
print('')

#Update latest quantity for product2 - from previous order, 300 -> 250 from order of 50
print('After order of 50, availableQuantity is reduced from 300 -> 250')
print('')
update_quantity_3 = '''
curl --location --request POST "localhost:5000/inventory" \
--form "availableQuantity=250" \
--form "productID=2" '''
os.system(update_quantity_3)
print('')

#Retrieve current quantitys
print('Getting latest inventory available quantity of products including change in Product2')
print('')
get_quantity = '''
curl --location --request GET "localhost:5000/inventory"
'''
os.system(get_quantity)
print('')


# And a separate REST endpoint that shows Top Selling products
print('Show top selling products (ProductID, Quantity Ordered)')
#Top sales
top_sales = '''
curl --location --request GET "localhost:5000/sales/all"
'''
os.system(top_sales)
