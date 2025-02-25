# Quorum Coding Challenge

Project created to work with legislative data (link: https://github.com/Ssoppa/quorum-coding-challenge).

## Cloning this Repo?

To run this project, you need to have installed Python (I'm using version 3.8.10) with the venv module.

Run the following at the root of your project:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or, if you are using Windows:

```
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

Then, using the just created virtual environment, run:

```
python main.py
```

Hopefully, a new file will appear in your folder, with the correct data.

### Choosing a Deliverable

You can specify the actions perfomed by providing the optional arguments. You can use the help flag to see details about them.

```
python main.py -h
```

You can specify each file path, as well as the desired deliverable. For example, for the deliverable 1, based on the provided description:

```
python main.py --bills_path bills.csv --legislators_path legislators.csv --votes_path votes.csv --vote_results_path vote_results.csv --output_path legislators-support-oppose-count.csv --deliver_mode 1
```

And for the second deliverable:

```
python main.py --bills_path bills.csv --legislators_path legislators.csv --votes_path votes.csv --vote_results_path vote_results.csv --output_path bills.csv --deliver_mode 2
```
