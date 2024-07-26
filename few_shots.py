few_shots = [
   {'Question': "How many t-shirts do we have left for the nike in extra small size and white color?",
    'SQLQuery': "SELECT SUM(stock_quantity ) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
    'SQLResult': "Result of the SQL query",
    'Answer': '10'},
    {'Question': "How much is the price of the inventory for all small size t-shirts?",
    'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
    'SQLResult': "Result of the SQL query",
    'Answer': '20068'},
    {'Question': "If we have to sell all the Levi's T-shirts today woth discounts applied. How much revenue our store will generate (post discounts)?",
    'SQLQuery': """
    SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount, 0))/100)) as total_revenue
from (SELECT sum(price*stock_quantity) as total_amount, t_shirt_id 
from t_shirts where brand = 'Levi'
GROUP BY t_shirt_id)a 
LEFT JOIN discounts on a.t_shirt_id = discounts.t_shirt_id
    """,
    'SQLResult': "Result of the SQL query",
    'Answer': '25434.7'},
    {'Question': "If we have to sell all the Levi's T-shirts today. How much revenue our store will get?",
    'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
    'SQLResult': "Result of the SQL query",
    'Answer': '28811'},
    {'Question': "How many white color Levi's t_shirts we have available?",
    'SQLQuery': """
SELECT SUM(stock_quantity )
FROM t_shirts 
WHERE brand = 'Levi' AND color = 'White'
""",
    'SQLResult': "Result of the SQL query",
    'Answer': '253'},
]