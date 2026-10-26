# Titanic dataset notes

## Source

This is the Titanic sample CSV used in the seaborn examples:

- [Source file](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv)
- [Raw source CSV](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv)
- [Source repository](https://github.com/mwaskom/seaborn-data)

The source repository describes itself as a collection for seaborn examples rather than a general-purpose data archive. This lesson retains source attribution and includes the same snapshot for reproducible educational examples. We do not assert a new license for the underlying records.

## Size and unit of observation

891 rows, 15 columns. One row represents one passenger record in this sample. This is not a census of everyone aboard.

## Columns used in the lesson

| Column | Meaning | Teaching role |
| --- | --- | --- |
| `sex` | Sex category recorded in the source | Nominal category |
| `embark_town` | Recorded embarkation town | Nominal category |
| `class` | First, Second, or Third passenger class | Ordinal category |
| `pclass` | Numeric passenger-class code | Number representing a category |
| `survived` | 0 = did not survive, 1 = survived | Binary outcome |
| `sibsp` | Number of siblings and spouses aboard | Discrete count |
| `parch` | Number of parents and children aboard | Discrete count |
| `age` | Recorded age in years | Continuous measurement |
| `fare` | Recorded fare amount | Numerical measurement |

`survival` is a readable label column derived in the lesson from `survived`; it is not an additional source field. A zero `sibsp` does not necessarily mean travelling alone, because parents or children may have been aboard.

## Missing values and interpretation

- `age`: 177 missing values; 714 recorded ages.
- `deck`: 688 missing values.
- `embarked` and `embark_town`: 2 missing values each.

The age subset may differ from the full sample. Charts describe associations and do not establish causation. Fare should not automatically be interpreted as an independently paid ticket price for each passenger. No genuine time column is present, so row order is not treated as time.
