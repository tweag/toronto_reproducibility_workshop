from collections import Counter
from datetime import datetime

from celluloid import Camera
from dateutil.relativedelta import relativedelta
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# split list of genres
df['listed_in'] = df['listed_in'].apply(
    lambda x: [y.strip() for y in x.split(",")])

# find ten most common genres
all_genres = [x for z in df['listed_in'] for x in z]
c = Counter(all_genres)
mc = c.most_common()
mc_genres = [x[0] for x in mc]
mc_genres.remove('International Movies')
mc_genres.remove('International TV Shows')
ten_mc_genres = mc_genres[:10]

# clean data and format date column
df = df.sort_values("date_added")
df = df[~df["date_added"].isnull()]
df["date_added"] = df["date_added"].apply(lambda x: x.strip())
df["date_added"] = pd.to_datetime(df["date_added"], format="%B %d, %Y")
df = df[[x.year >= 2016 for x in df['date_added']]]

# count how many movies were added in each genre, for quartals
counters = []
dates = [datetime(2016, 1, 1)]
last_date = datetime(2021, 3, 1)
while (next_date := dates[-1] + relativedelta(months=+3)) < last_date:
    dates.append(next_date)
date_ranges = list(zip(dates[:-1], dates[1:]))
for dt1, dt2 in date_ranges:
    filtered = df[(dt1 <= df["date_added"]) & (df["date_added"] < dt2)]
    all_genres = [x for y in filtered['listed_in'] for x in y]
    counters.append(Counter(all_genres))

# make movie
fig, ax = plt.subplots()
camera = Camera(fig)
for (dt1, dt2), counter in zip(date_ranges, counters):
    xses = np.arange(1, len(ten_mc_genres) + 1)
    num_movies = np.array([counter[genre] for genre in ten_mc_genres])
    num_movies = num_movies / sum(num_movies)
    ax.bar(xses, num_movies, color="blue")
    ax.set_xticks(xses)
    ax.set_xticklabels(ten_mc_genres, rotation=60)
    ax.text(5, 0.275, f"{dt1.strftime('%b, %Y')} - {dt2.strftime('%b, %Y')}",
            fontsize=20)
    ax.set_ylabel("fraction of released movies")
    ax.set_title("New movies added by genre")
    fig.tight_layout()
    camera.snap()
anim = camera.animate(blit=True)
anim.save("test.mp4", fps=2)
