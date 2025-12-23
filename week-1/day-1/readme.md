# Day 1–Day 10: Detailed StepnbynStep Plan

This 10nday plan combines learning and doing in parallel. Each day you will touch Python, SQL,
Excel, and a BI tool (Power BI or Tableau) on the SAME core project: a Pharma Sales & Safety
Analytics System. Assume 6–8 hours per day. Adjust up/down to your pace.

# Day 1 – Get Comfortable With the Data

Goal: Set up the dataset and touch all four tools: Python, SQL, Excel, and BI using the same
pharma_sales.csv file.

## StepnbynStep Tasks:

- Setup (30–45 min): Create a folder for the project. In Excel, create a file named
    pharma_sales.csv with columns Date, Product, Region, Quantity, Revenue and at least 20–
    rows of example data. Save as CSV.
- Python – Load & Inspect (1.5–2 hrs): Open Jupyter/VS Code, create day1_python.ipynb,
    import pandas, load the CSV with pd.read_csv(), run head(), info(), describe(), then create a
    new column Price_per_unit = Revenue / Quantity and filter rows with Revenue > 10000.
- SQL – Basic SELECT (1–1.5 hrs): Create/import table pharma_sales from the CSV in
    SQLite/MySQL. Run SELECT *; SELECT specific columns (Date, Product, Revenue); apply
    WHERE Region='North' and WHERE Revenue>10000; use LIMIT to view a subset.
- Excel – Basic Summary (1–1.5 hrs): Open the CSV in Excel, convert to a Table, use SUM,
    AVERAGE, MAX, MIN on Revenue and Quantity; apply Filter and Sort (e.g., highest Revenue
    first).
- BI Tool – First Charts (1–1.5 hrs): In Power BI/Tableau, import pharma_sales.csv and build
    two visuals: Revenue by Product and Revenue by Region as bar/column charts.
- Notes (20–30 min): Create a notes file (e.g., day1_notes.txt) summarizing commands, queries,
    formulas, and screenshots you created.

## EndnofnDay Deliverables (You should have):

- pharma_sales.csv with at least 20–50 rows of data.
- day1_python.ipynb with CSV load, inspection, a filter, and a new column.
- day1_sql.sql file with SELECT and WHERE examples.
- day1_excel.xlsx with basic summaries and filters applied.
- day1_dashboard.pbix (or Tableau workbook) with at least 2 visuals.
- day1_notes.txt summarizing what you did and learned.