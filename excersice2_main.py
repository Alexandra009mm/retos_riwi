from feature_customer_register import customer_register
from feature_product_register import product_register
from feature_order_creation import order_creation
from feature_check_orders import check_orders
from feature_daily_calculator import daily_income
from feature_final_report import final_report

customer_dic = {}
products_tuple = ()
order_tuple = ()

customer_register(customer_dic)

products_tuple = product_register(products_tuple)

order_tuple = order_creation(customer_dic, products_tuple, order_tuple)

check_orders(order_tuple)

daily_income(order_tuple)

final_report(order_tuple)