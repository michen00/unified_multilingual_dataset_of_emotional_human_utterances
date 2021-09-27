"""With the multilingual_speech_valence_classification_datasets downloaded, this script renames each file listed in aggregate_data_files.tsv and copies them to data/interim/."""

from shutil import copyfile

prefix_path = "data/multilingual_speech_valence_classification_datasets/datasets/"
in_file = "aggregate_data_files.tsv"
with open(f"{prefix_path}{in_file}", "r") as f:
    count = 0
    for record in f.readlines():
        (
            path,
            emo,
            valence,
            lang1,
            lang2,
            speaker,
            gender,
            dataset,
        ) = record.strip().split("\t")
        new_file = "+".join(
            _.replace("+", ".").replace("/", ")")
            for _ in (
                f"{count:05}",
                dataset,
                speaker,
                gender,
                emo,
                valence,
                lang1,
                lang2,
            )
        )
        copyfile(
            f"{prefix_path}{path}",
            f"data/interim/{new_file}.{path.rsplit('.', maxsplit=1)[-1]}",
        )
        count += 1

print("done")
