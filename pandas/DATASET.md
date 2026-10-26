# Dataset source and notes

`malayalam_movies_tutorial.csv` contains 187 films and 15 columns, with release years from 1954 to 2026. It is the curated teaching subset used in this video.

Source: [Wikidata Query Service](https://query.wikidata.org/), extracted on 9 October 2026. This is structured Wikidata metadata, not a scrape of Wikipedia article text. Each row includes its source item’s `wikidata_url`.

## Permission

Wikidata structured data is released under [CC0](https://www.wikidata.org/wiki/Wikidata:Licensing). [CC0 public-domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).

Suggested credit: **Movie metadata: Wikidata (CC0), extracted 9 October 2026.** This does not license film posters, movie clips, soundtracks or Wikipedia article prose.

## Column dictionary

| Column | Kind | Meaning |
| --- | --- | --- |
| wikidata_id | identifier | Stable film item ID; unique in each CSV |
| title | text | English label, falling back to Malayalam |
| release_year | discrete / temporal | Earliest recorded publication year, excluding dates after extraction date |
| decade | categorical / ordered | Derived from release_year, e.g. 2010s |
| director | categorical, potentially multiple | Recorded director labels, separated by a vertical bar |
| director_count | discrete count | Distinct director items recorded in Wikidata |
| genre | categorical, potentially multiple | Recorded genres, separated by a vertical bar |
| composer | categorical, potentially multiple | Recorded composers |
| production_company | categorical, potentially multiple | Recorded companies; very sparse |
| runtime_minutes | continuous measurement | Duration converted to minutes; often recorded to whole minutes |
| runtime_hours | continuous measurement, derived | runtime_minutes / 60 rounded to four decimals; not an independent variable |
| cast_recorded_count | discrete count | Number of distinct cast items recorded; NOT the complete cast size |
| awards_recorded_count | discrete count | Distinct award items recorded on the film; NOT its total awards won |
| cast | categorical list | Recorded cast labels, separated by a vertical bar |
| wikidata_url | provenance | Direct link to the film record |


## Selection and limitations

- Malayalam-language film items in Wikidata, with a recorded director and a usable recorded runtime. This can include multilingual productions.
- One row per Wikidata film identifier. Multiple names are joined with ` | `.
- Release year is the earliest recorded publication year and may represent a festival release.
- Durations are converted to minutes. Values outside 40–300 minutes and conflicting remaining duration claims are left blank before selecting the teaching subset. This is a selection rule, not verification that every retained value is correct.
- Blank means unrecorded or unusable, not zero. Recorded cast and award counts can be incomplete; they are not complete cast sizes or lifetime award totals.
- This is a convenience sample for practising Pandas, not a representative dataset of all Malayalam cinema. Film details can be incomplete or wrong in the source. No ratings, revenue or budgets were invented.
- `runtime_hours` is derived from `runtime_minutes`; it is not an independent measurement.
