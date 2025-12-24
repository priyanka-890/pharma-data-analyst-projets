# to get dayname out of date
to_chat(order_date,'day')

# extract daynumber out of order_date
EXTRACT(DOW FROM order_date)