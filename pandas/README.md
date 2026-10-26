# Learn Pandas with Malayalam movie data

Follow along with the Malayalam beginner tutorial in the **Python for Data Science** YouTube playlist.

## Files

- `malayalam_movies_tutorial.csv`: the exact 187-film, 15-column dataset used in the lesson.
- `pandas_tutorial.py`: lesson code, including explicit commands to inspect changes.
- `requirements.txt`: Python packages; Pandas is pinned to the version used for recording.
- `DATASET.md`: column meanings, source and data limitations.

## Get started

1. Download the repository ZIP using **Code → Download ZIP** on the repository home page.
2. Extract it and open the **pandas** folder in VS Code.
3. Install the Python and Jupyter extensions in VS Code, and select your Python environment.
4. From a terminal in this folder, install the packages:

```bash
python -m pip install -r requirements.txt
```

5. Open `pandas_tutorial.py`. Select a complete statement (including all lines of a multiline expression), then press **Shift+Enter** to execute it in the Interactive Window. Start at the top and work downward so the variables exist.
6. Keep `malayalam_movies_tutorial.csv` in the working directory. Verify the folder with:

```python
from pathlib import Path
print(Path.cwd())
```

The working directory can differ from the script’s folder. If the CSV is elsewhere, copy its full path into `pd.read_csv(...)`; a commented example is included in the code.

## Practice ideas

Change the actor filter between Mohanlal and Mammootty, vary the minimum release year, build your watchlist and compare runtime summaries. These are comparisons within this small dataset, not career rankings or acting-quality scores.

## Exports

The code writes your watchlist and summary CSVs into `tutorial_exports/` in the working directory.

## Source and permission

Movie metadata comes from **Wikidata**, the structured sister project of Wikipedia, extracted on 9 October 2026. Wikidata structured data is **CC0**. The dataset is provided for learning and can contain missing or incorrect source values. See [DATASET.md](DATASET.md).
