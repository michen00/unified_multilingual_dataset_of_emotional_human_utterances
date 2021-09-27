"""This script writes the filenames in data/preprocessed and their durations to manifest.tsv."""

from librosa import get_duration
from numpy import mean, std
from os import walk
from tqdm import tqdm

data_folder = "../data/preprocessed"

durations = []
with open("manifest.tsv", "w") as f:
    for _, _, files in walk(data_folder):
        for file_ in tqdm(files):
            durations.append(
                duration := get_duration(filename=f"{data_folder}/{file_}")
            )
            f.write("\t".join((file_, str(duration), "\n")))

print(f"processed {len(durations)} audio file(s)")
print("total duration in seconds:", sum(durations))
print(f"average duration: {mean(durations)} ({std(durations)})")
print("shortest:", min(durations))
print("longest:", max(durations))
print()
print("done")
