import pandas as pd

vote_results_df = pd.read_csv('vote_results.csv')
legistators_df = pd.read_csv('legislators.csv')
votes_df = pd.read_csv('votes.csv')
bills_df = pd.read_csv('bills_input.csv')

full_df = vote_results_df.join(legistators_df.set_index('id'), on='legislator_id')
full_df = full_df.join(votes_df.set_index('id'), on='vote_id')
full_df = full_df.join(bills_df.set_index('id'), on='bill_id')

# first question (15 min)
first_question_data = []
for legislator_id, legislator_name in legistators_df.values:
  counts = full_df[full_df['legislator_id'] == legislator_id]['vote_type'].value_counts()
  num_supported_bills = counts[1] if 1 in counts else 0
  num_opposed_bills = counts[2] if 2 in counts else 0
  
  first_question_data.append([legislator_id, legislator_name, num_supported_bills, num_opposed_bills])
first_question_df = pd.DataFrame(first_question_data, columns=['id', 'name', 'num_supported_bills', 'num_opposed_bills'])
first_question_df.set_index('id').to_csv('legislators-support-oppose-count.csv')