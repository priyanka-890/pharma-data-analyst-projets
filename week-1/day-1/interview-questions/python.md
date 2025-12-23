# Python Interview Questions (Based on Day 1 Work)

 interview questions derived from the Pandas operations used in this project.

---

## 🔹 BASIC QUESTIONS

### 1. What does `pd.read_csv()` do?
Loads a CSV file into a pandas DataFrame for analysis.

---

### 2. What is a DataFrame?
A two-dimensional table-like data structure in pandas, similar to Excel or a SQL table.

---

### 3. What does `df.head()` do?
Displays the first 5 rows of the dataset.

---

### 4. What is `df.info()` used for?
Displays column names, data types, and non-null counts.

---

### 5. What is `df.describe()`?
Generates summary statistics like mean, min, max, and quartiles.

---

### 6. Why rename `salesdaily.csv` to `pharma_sales.csv`?
To improve clarity and project readability by using a domain-specific filename.

---

## 🔹 INTERMEDIATE QUESTIONS

### 7. What does this line do?

drug_cols = ['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R0]

Stores drug column names for easy referencing and scalability.
“It makes the code scalable. If new drug columns are added later, I only update the list instead of rewriting the logic. It also improves readability and reduces errors by referencing column names from one place.”

# df[drug_cols].sum(axis=1)

axis=0 → go down (column direction), sum each column

axis=1 → go across (row direction), sum each row

# df[df[total_sales]>50]

filters values>50

“It’s boolean indexing to extract high-sales records for analysis.”
