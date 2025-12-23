# these codes used in cols are
    They are WHO ATC classification(Anatomical Therapeutic Chemical Classification) codes used to group pharmaceuticals by therapeutic class. I don’t memorize codes, but I understand how they are structured and I can interpret them to analyze sales trends by drug category.

# data stored in data sets
    Pharma datasets often store data as:

    Defined Daily Dose (DDD)

    This is a WHO standard unit that represents:
        "The average daily dose used by an adult for that drug.”

## Sales Conversion Explanation

This dataset uses **standardized consumption units**, not raw pack or pill counts.  
Sales values may appear as decimals because they are normalized (e.g., by daily dose).

| Retail Sale Situation        | Converted Dataset Value |
|------------------------------|-------------------------|
| 1 person bought half a dose  | 0.5                     |
| 3 people bought full doses   | 3.0                     |
| Mixed strengths & quantities | 3.4                     |
| Many purchases combined      | 61.85                   |

