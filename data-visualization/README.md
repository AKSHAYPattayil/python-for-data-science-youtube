# Data visualization with Python

Companion materials for the Malayalam YouTube lesson: identify the variable type, choose a suitable chart, run the Python code, and interpret the result.

## Start here

- **[Open the notebook](data_visualization.ipynb)** — setup, dataset inspection, and 12 charts with saved outputs.
- **[Dataset CSV](titanic.csv)** — 891 passenger records and 15 columns.
- **[Python walkthrough](data_visualization.py)** — the same chart commands in a script.
- **[Dataset notes](DATASET.md)** — source, column meanings, and missing values.

Keep the CSV, notebook, and Python file together in this folder.

## Run in VS Code

1. Download this repository with **Code → Download ZIP**, then extract it.
2. Open the **data-visualization** folder in VS Code.
3. Choose a Python environment and install the packages:

   ```sh
   python -m pip install -r requirements.txt
   ```

4. Open `data_visualization.ipynb`, select that environment as the kernel, and run the setup cell first. Run the remaining cells one at a time.

The saved notebook outputs can be viewed on GitHub without running Python. VS Code needs its Python and Jupyter extensions to execute notebook cells.

Alternatively, run the complete script:

```sh
python data_visualization.py
```

Close each chart window to advance to the next chart when running the script. For VS Code's interactive window, execute imports and data preparation first, then select each complete plotting block through `plt.show()` and run it. When `__file__` is unavailable, the script uses the current working folder, so start in this lesson folder.

## What you will learn

| Variable or relationship | Example | Visualization |
| --- | --- | --- |
| Nominal category | `sex`, `embark_town` | Count plot |
| Ordered category | `class` | Count plot in a meaningful order |
| Binary outcome | `survived` / `survival` | Count plot and pie chart |
| Discrete count | `sibsp` | Integer-aligned histogram |
| Continuous measurement | `age` | Histogram and ECDF |
| Category + measurement | `class` and `age` | Box plot |
| Two measurements | `age` and `fare` | Scatter plot |
| Two categorical variables | `class` and `survival` | Grouped counts and within-class percentage bars |
| Several numerical variables | `age`, `fare`, `sibsp`, `parch` | Pearson correlation heatmap |

A numerical storage type does not automatically make a column a numerical measurement. For example, `pclass` and `survived` are category codes. The lesson also distinguishes counts from percentages and association from causation.

## Missing data

Age is missing in 177 records. Age-dependent plots use the 714 records with a recorded age. Other plots retain the records available for their own variables. This sample is not a complete list of everyone aboard the Titanic.

## Practice

Run the notebook again, read each chart's axes and labels, and explain the result in your own words. Try changing the age histogram's bin count and compare what changes.
