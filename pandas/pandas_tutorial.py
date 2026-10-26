# Keep malayalam_movies_tutorial.csv in the current working directory.

from pathlib import Path

import pandas as pd

from IPython.display import display

print("Pandas version:", pd.__version__)

pd.set_option("display.max_columns", 12)

pd.set_option("display.max_colwidth", 45)

titles = pd.Series(["Drishyam", "Premam", "Manjummel Boys"], name="title")
display(titles.head())

display(titles)

practice = pd.DataFrame({
    "title": ["Drishyam", "Premam", "Manjummel Boys"],
    "release_year": [2013, 2015, 2024],
})
display(practice.head())

display(practice)

print("Current working directory:", Path.cwd())

raw = pd.read_csv("malayalam_movies_tutorial.csv", encoding="utf-8-sig")
# File elsewhere? Copy its full path and use that instead (example only):
# raw = pd.read_csv(r"C:\Users\YourName\Downloads\malayalam_movies_tutorial.csv", encoding="utf-8-sig")
display(raw[["title", "release_year", "runtime_minutes"]].head())

movies = raw.copy()  # Keep the loaded source unchanged.
display(movies[["title", "release_year", "runtime_minutes"]].head())

EXPORT_DIR = Path("tutorial_exports")

display(movies.head())

print("Rows, columns:", movies.shape)

print("Columns:", movies.columns.tolist())

display(movies.tail(3))

display(movies.sample(4, random_state=42))

display(movies.dtypes)

movies.info()

display(movies["title"].head(3))

display(movies[["title", "release_year", "runtime_minutes"]].head(5))

display(movies.loc[0:2, ["title", "director"]])  # Includes label 2.

display(movies.iloc[0:2, 0:4])  # Positions 0 and 1 only.

by_id = movies.set_index("wikidata_id")
display(by_id[["title", "director"]].head())

first_id = movies.loc[0, "wikidata_id"]

display(by_id.loc[[first_id], ["title", "director"]])

print("Scalar by label:", by_id.at[first_id, "title"])

print("Scalar by position:", movies.iat[0, 1])

display(by_id.reset_index().head(2))

FAVOURITE_ACTOR = "Mohanlal"

MIN_YEAR = 2000

actor_mask = movies["cast"].str.contains(FAVOURITE_ACTOR, case=False, regex=False, na=False)

favourites = movies.loc[
    actor_mask & (movies["release_year"] >= MIN_YEAR),
    ["title", "release_year", "runtime_minutes", "director"],
]
display(favourites[["title", "release_year", "runtime_minutes"]].head())

print(f"{FAVOURITE_ACTOR}: {len(favourites)} recorded matches since {MIN_YEAR}")

display(favourites)

display(movies.loc[movies["release_year"].between(2010, 2020), ["title", "release_year"]].head())

display(movies.loc[movies["release_year"].isin([2013, 2015, 2024]), ["title", "release_year"]].head())

display(movies.query("release_year >= @MIN_YEAR and runtime_minutes < 120")[["title", "runtime_minutes"]].head())

TOP_N = 5

longest = movies.sort_values(
    ["runtime_minutes", "title"], ascending=[False, True]
).head(TOP_N).reset_index(drop=True)
display(longest[["title", "runtime_minutes"]].head())

display(longest[["title", "release_year", "runtime_minutes"]])

display(movies.nlargest(3, "runtime_minutes")[["title", "runtime_minutes"]])

working = movies.copy()
display(working[["title", "runtime_minutes"]].head())

working["runtime_original"] = working["runtime_minutes"].copy()
display(working[["title", "runtime_minutes", "runtime_original"]].head())

working["hours_calculated"] = (working["runtime_minutes"] / 60).round(2)
display(working[["title", "runtime_minutes", "hours_calculated"]].head())

working["runtime_band"] = "Up to 150 minutes"
display(working[["title", "runtime_minutes", "runtime_band"]].head())

working.loc[working["runtime_minutes"] > 150, "runtime_band"] = "Over 150 minutes"
display(working[["title", "runtime_minutes", "runtime_band"]].head())

renamed = working.rename(columns={"title": "movie_name"})
display(renamed[["movie_name", "hours_calculated", "runtime_band"]].head())

display(renamed[["movie_name", "hours_calculated", "runtime_band"]].head())

working = working.drop(columns=["runtime_original", "hours_calculated"])
print(working.columns.tolist())

print("Source still has its original columns:", raw.shape)

display(movies.isna().sum().sort_values(ascending=False))

display(movies.loc[movies["genre"].isna(), ["title", "genre"]].head())

known_genres = movies.dropna(subset=["genre"]).copy()
display(known_genres[["title", "genre"]].head())

genre_for_display = movies["genre"].fillna("Not recorded")
display(genre_for_display.head())

print("Rows with genre:", len(known_genres))

print("Duplicate film IDs:", movies.duplicated(subset=["wikidata_id"]).sum())

unique_movies = movies.drop_duplicates(subset=["wikidata_id"]).copy()
display(unique_movies[["wikidata_id", "title"]].head())

movies["cast_recorded_count"] = pd.to_numeric(movies["cast_recorded_count"], errors="coerce").astype("Int64")
display(movies["cast_recorded_count"].head())

movies["director_count"] = movies["director_count"].astype("Int64")
display(movies["director_count"].head())

dirty = pd.DataFrame({"title": ["  Premam  ", "Drishyam", "Drishyam"], "runtime_text": ["156", "unknown", "unknown"]})
display(dirty.head())

dirty["title"] = dirty["title"].str.strip()
display(dirty.head())

dirty["runtime_numeric"] = pd.to_numeric(dirty["runtime_text"], errors="coerce")
display(dirty[["title", "runtime_text", "runtime_numeric"]].head())

display(dirty.drop_duplicates())

print("Titles containing 'Drishyam':")

display(movies.loc[movies["title"].str.contains("Drishyam", case=False, regex=False, na=False), ["title", "release_year"]])

NICKNAME = "Lalettan"

nickname_lookup = {"Lalettan": "Mohanlal", "Mammookka": "Mammootty"}

print(pd.Series([NICKNAME]).map(nickname_lookup).iloc[0])

def runtime_label(minutes):
    if pd.isna(minutes):
        return "Unknown"
    if minutes < 120:
        return "Under 2 hours"
    if minutes <= 150:
        return "2 to 2.5 hours"
    return "Over 2.5 hours"

movies["runtime_group"] = movies["runtime_minutes"].apply(runtime_label)
display(movies[["title", "runtime_group"]].head())

movies["watchlist_label"] = movies.apply(
    lambda row: f"{row['title']} ({row['release_year']})", axis=1
)
display(movies[["title", "release_year", "watchlist_label"]].head())

movies["hours_recomputed"] = movies["runtime_minutes"].div(60)
display(movies[["title", "runtime_minutes", "hours_recomputed"]].head())

display(movies[["watchlist_label", "runtime_group", "hours_recomputed"]].head())

display(movies[["runtime_minutes", "cast_recorded_count"]].describe())

print("Median runtime:", movies["runtime_minutes"].median())

display(movies["runtime_group"].value_counts())

display(movies["director"].value_counts().head(5))

display(movies.groupby("decade")["runtime_minutes"].mean().round(1))

display(movies.groupby("decade")["runtime_minutes"].agg(["count", "mean", "median", "min", "max"]).round(1))

decade_summary = movies.groupby("decade", as_index=False).agg(
    movie_count=("wikidata_id", "size"),
    average_runtime=("runtime_minutes", "mean"),
    median_runtime=("runtime_minutes", "median"),
    maximum_runtime=("runtime_minutes", "max"),
)
display(decade_summary.round(1).head())

display(decade_summary.round(1))

comparison_rows = []

for actor in ["Mohanlal", "Mammootty"]:
    selected = movies.loc[movies["cast"].str.contains(actor, regex=False, na=False)]
    comparison_rows.append({"actor": actor, "films_in_sample": len(selected), "mean_runtime": selected["runtime_minutes"].mean()})

actor_comparison = pd.DataFrame(comparison_rows)
display(actor_comparison.round(1))

display(actor_comparison.round(1))

print("Sample matches only; no career ranking or measure of acting quality.")

pivot = movies.pivot_table(
    index="decade",
    columns="runtime_group",
    values="wikidata_id",
    aggfunc="count",
    fill_value=0,
    observed=True,
)
display(pivot.head())

display(pivot)

counts_long = movies.groupby(["decade", "runtime_group"], observed=True).size().reset_index(name="movie_count")
display(counts_long.head())

counts_wide = counts_long.pivot(index="decade", columns="runtime_group", values="movie_count").fillna(0)
display(counts_wide.head())

display(counts_wide)

WATCH_ACTOR = "Mammootty"

WATCH_AFTER_YEAR = 2000

MAX_MINUTES = 160

watchlist = movies.loc[
    movies["cast"].str.contains(WATCH_ACTOR, case=False, regex=False, na=False)
    & movies["release_year"].ge(WATCH_AFTER_YEAR)
    & movies["runtime_minutes"].le(MAX_MINUTES),
    ["wikidata_id", "title", "release_year", "director", "runtime_minutes"],
].sort_values(["runtime_minutes", "title"]).reset_index(drop=True)
display(watchlist[["title", "release_year", "runtime_minutes"]].head())

print(f"Found {len(watchlist)} matches for {WATCH_ACTOR}")

display(watchlist)

EXPORT_DIR.mkdir(exist_ok=True)

export_path = EXPORT_DIR / "my_movie_watchlist.csv"

watchlist.to_csv(export_path, index=False, encoding="utf-8-sig")

decade_summary.to_csv(EXPORT_DIR / "runtime_by_decade.csv", index=False, encoding="utf-8-sig")

reloaded = pd.read_csv(export_path, encoding="utf-8-sig")

assert list(reloaded.columns) == list(watchlist.columns)

assert len(reloaded) == len(watchlist)

print("Saved:", export_path)

display(reloaded.head())
