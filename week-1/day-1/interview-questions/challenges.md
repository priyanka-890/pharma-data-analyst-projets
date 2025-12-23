# copying data into pharma_sales table
-this is correct query
“Dates in this session are written as Month / Day / Year.”

SET datestyle = 'MDY';

COPY pharma_sales
FROM 'C:/data/pharma_sales.csv'
DELIMITER ','
CSV HEADER;


1.faced permission issues as used users location got permissiondenied but got suceeded by moving to c:/


2.postgress takes take dateas MDY "need to chnge in that format"



