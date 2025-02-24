import pandas as pd

vote_results_df = pd.read_csv('vote_results.csv')
legistators_df = pd.read_csv('legislators.csv')
votes_df = pd.read_csv('votes.csv')
bills_df = pd.read_csv('bills_input.csv')

full_df = vote_results_df.join(legistators_df.set_index('id'), on='legislator_id')
full_df = full_df.join(votes_df.set_index('id'), on='vote_id')
full_df = full_df.join(bills_df.set_index('id'), on='bill_id')

# second question (1.5h)
second_question_data = []
for bill_id, bill_title, bill_sponsor_id in bills_df.values:
  sponsor_list = list(legistators_df[legistators_df["id"] == bill_sponsor_id]["name"])
  sponsor_name = sponsor_list[0] if len(sponsor_list) > 0 else "Unknown"

  counts = full_df[full_df['bill_id'] == bill_id]['vote_type'].value_counts()
  supporter_count = counts[1] if 1 in counts else 0
  opposer_count = counts[2] if 2 in counts else 0

  second_question_data.append([bill_id, bill_title, supporter_count, opposer_count, sponsor_name])

second_question_df = pd.DataFrame(second_question_data, columns=['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor'])
second_question_df.set_index('id').to_csv('new_bills.csv')
