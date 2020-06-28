import os

#Create latest quantity for product1
print('Inserting productID1 to DB')
print('')
update_quantity_1 = '''
curl --location --request POST "localhost:5000/inventory" \
--form "availableQuantity=55" \
--form "productID=1" '''
os.system(update_quantity_1)
print('')

#Create latest quantity for product2
print('Inserting productID2 to DB')
print('')
update_quantity_2 = '''
curl --location --request POST "localhost:5000/inventory" \
--form "availableQuantity=90" \
--form "productID=2" '''
os.system(update_quantity_2)
print('')

#Update latest quantity for product2 - Mass order
print('Inserting new record for productID2 to DB')
print('')
update_quantity_3 = '''
curl --location --request POST "localhost:5000/inventory" \
--form "availableQuantity=3" \
--form "productID=2" '''
os.system(update_quantity_3)
print('')

#There should be a separate REST endpoint that shows the latest available quantity of product in stock
#Retrieve current quantitys
print('Getting latest available quantity of products (ProductID, Quantity Available)')
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
curl --location --request GET "localhost:5000/sales"
'''
os.system(top_sales)
