1. Imported Data into Power BI

Loaded dataset day1_output.csv.

Verified that numerical columns (M01AB → R06) and the date column datum were recognized correctly.

Confirmed that Power BI automatically created a Date Hierarchy, which initially caused confusion.

⚙️ 2. Disabled Auto Date/Time (Important for Clean Modeling)

Power BI was automatically generating Year–Quarter–Month–Day hierarchies.

To prevent this:

File → Options → Data Load → Uncheck “Auto date/time for new files”

This allowed full control over date calculations.

🧮 3. Created Date-Based Columns (Using DAX)

Since the built-in hierarchy was removed, we manually created our own:

✔ a. Weekday Name
weekdayname_2 = FORMAT('day1_output'[datum], "dddd")


This created labels like Monday, Tuesday, etc.

✔ b. Weekday Number (Needed for Sorting)
weekdayNumber = WEEKDAY('day1_output'[datum], 2)


This returns:

1 = Monday

2 = Tuesday

...

7 = Sunday

🔢 4. Corrected Sorting Order of Weekdays

Problem: The bar chart sorted weekdays alphabetically.

Solution:
Use Sort By Column:

Go to Model View

Select column weekdayname_2

In Properties → Sort by column → weekdayNumber

Now weekday order correctly appears:

Monday → Tuesday → Wednesday → Thursday → Friday → Saturday → Sunday

📊 5. Built Data Visualizations
✔ A. Line Chart (Total Sales Over Time)

X-axis: datum

Y-axis: Sum of Total_sales

Shows sales trend across the entire date range.

✔ B. Bar Chart (Total Sales by Weekday)

Axis: weekdayname_2

Values: Sum of Total_sales

Sorted using weekdayNumber

After fixing sorting, the bar chart displayed days in natural order.

✔ 6. Verified Calculated Columns in Data View

Confirmed:

weekdayname_2 is labeled correctly (Monday, Tuesday…)

weekdayNumber values are correct (1–7)

Confirmed these fields are available in the Report View.

🚧 7. Challenges Faced & How They Were Solved
1. Only “Date Hierarchy” appeared — no raw date column

Solution: Disabled Auto Date/Time

Then used raw datum column for visualizations.

2. Could not find “Sort By Column” option

Because it only appears in Model View, not in Report View.

Once in Model View, the option appeared in the Properties panel.

3. Weekday order was incorrect

Weekdays were sorted alphabetically:

Friday, Monday, Saturday, Sunday, etc.

Fix: Linked weekdayname_2 to weekdayNumber using Sort by Column.

4. Visual not showing all days

Chart was small, required resizing.

Rechecked axis fields and sorting.

5. DAX formulas initially created errors

Corrected syntax and re-entered:

FORMAT() for name

WEEKDAY() for number

🏁 Final Deliverables Created in Power BI
✔ A clean data model with:

weekdayname_2

weekdayNumber

Year, Month, Hour (auto-generated/verified)

✔ Visuals:

Line Chart: Date vs Total Sales

Bar Chart: Weekday vs Total Sales

✔ Sorting + Formatting:

Natural weekday order

Fully functioning date-based analysis

⭐ Day 1 Power BI Summary (One Sentence)

You successfully learned how to model dates, build DAX columns, fix sorting logic, and create meaningful visualizations—overcoming real Power BI beginner challenges.

If you'd like, I can also create:

📘 Day 2 Plan – What to Learn Next
📊 Full Power BI Dashboard
📚 README for Excel + Power BI combined

Just tell me!

DEVELOPER MODE