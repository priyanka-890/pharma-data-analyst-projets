# part 1

import flat csv file-----------into pgsql or ms sql ------------>create a db----------fire sql queries------------create  a report


## part 2

import flat csv file or connect to ms sql or pgsql(industry standards)------into excel------->data cleaning-------data processing(formulas to manipulate data)------------------>data analysis(create pivot tables)---------->data visualisation(use pivot tables to build report or dash board)


# pgsql
CREATE TABLE pizza_sales_staging (
  pizza_id          TEXT,
  order_id          TEXT,
  pizza_name_id     TEXT,
  quantity          TEXT,
  order_date        TEXT,
  order_time        TEXT,
  unit_price        TEXT,
  total_price       TEXT,
  pizza_size        TEXT,
  pizza_category    TEXT,
  pizza_ingredients TEXT,
  pizza_name        TEXT
);

text no length
varchar(5) length of charactere mentioned