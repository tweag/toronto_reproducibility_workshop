# Analyzing Netflix movie genres

This groundbreaking analysis creates a video which shows how the genres of movies added to Netflix change over time.

## Data

The toy project requires the [Kaggle dataset on Netflix movies and TV shows](https://www.kaggle.com/shivamb/netflix-shows) saved as `netflix_titles.csv` in the `toy_project` folder.
I'm unsure about the license, so I did not include the actual CSV file.

## Installation
(This is intentionally vague to demonstrate the issue of unprecisely specified dependencies)

This script requires Python 3, a standard stack of data science Python modules and also FFMPEG. You can install the Python dependencies in a virtual environment via
```bash
$ python3 -m venv .venv
$ pip install -r requirements.txt
```
On Ubuntu, you can install FFMPEG by typing
```bash
$ sudo apt-get install ffmpeg
```

## Using the Nix shell
Install Nix according to the [instructions on the Nix website](https://nixos.org/download.html) (it's really a single command, if you're using Linux). Then run
```bash
$ nix-shell
```
and Nix will download the *full* dependency tree of the software environment declared in the `shell.nix` file. Once this is done, run the analysis script via
```bash
$ python3 analyse.py
```
and enjoy the fully reproducibly generated video saved as `test.mp4`.
