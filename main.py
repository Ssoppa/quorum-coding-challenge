import argparse
import pandas as pd


class BillVisualizator():
  def __init__(self, bills_path: str = "", legislators_path: str = "", votes_path: str = "", vote_results_path: str = ""):
    # Set all variables
    self.bills_path = bills_path
    self.legislators_path = legislators_path
    self.votes_path = votes_path
    self.vote_results_path = vote_results_path

    self.prepare_data()

  def prepare_data(self):
    print("Preparing data.")

    self.legistators_df = pd.read_csv(self.legislators_path)
    self.bills_df = pd.read_csv(self.bills_path)
    self.votes_df = pd.read_csv(self.votes_path)
    self.vote_results_df = pd.read_csv(self.vote_results_path)

    self.full_df = self.vote_results_df.join(self.legistators_df.set_index('id'), on='legislator_id').join(self.votes_df.set_index('id'), on='vote_id').join(self.bills_df.set_index('id'), on='bill_id')

  def get_first_deliverable(self, output_path: str = "output.csv"):
    print("Generating first deliverable.")
    
    first_question_data = []
    for legislator_id, legislator_name in self.legistators_df.values:
      counts = self.full_df[self.full_df['legislator_id'] == legislator_id]['vote_type'].value_counts()
      num_supported_bills = counts[1] if 1 in counts else 0
      num_opposed_bills = counts[2] if 2 in counts else 0

      first_question_data.append([legislator_id, legislator_name, num_supported_bills, num_opposed_bills])
      
    first_question_df = pd.DataFrame(first_question_data, columns=['id', 'name', 'num_supported_bills', 'num_opposed_bills'])
    first_question_df.set_index('id').to_csv(output_path)

    print("First deliverable created.")

  def get_second_deliverable(self, output_path: str = "output.csv"):
    print("Generating second deliverable.")
    
    second_question_data = []
    for bill_id, bill_title, bill_sponsor_id in self.bills_df.values:
      sponsor_list = list(self.legistators_df[self.legistators_df["id"] == bill_sponsor_id]["name"])
      sponsor_name = sponsor_list[0] if len(sponsor_list) > 0 else "Unknown"

      counts = self.full_df[self.full_df['bill_id'] == bill_id]['vote_type'].value_counts()
      supporter_count = counts[1] if 1 in counts else 0
      opposer_count = counts[2] if 2 in counts else 0

      second_question_data.append([bill_id, bill_title, supporter_count, opposer_count, sponsor_name])

    second_question_df = pd.DataFrame(second_question_data, columns=['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor'])
    second_question_df.set_index('id').to_csv(output_path)

    print("Second deliverable created.")

# Main function
if __name__ == "__main__":
  try:
    print("Starting program.")
    
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--bills_path', action = 'store', dest = 'bills_path', default='bills_input.csv', required = False, help = 'Filepath to bills csv file.')
    parser.add_argument('--legislators_path', action = 'store', dest = 'legislators_path', default='legislators.csv', required = False, help = 'Filepath to legislators csv file.')
    parser.add_argument('--votes_path', action = 'store', dest = 'votes_path', default='votes.csv', required = False, help = 'Filepath to votes csv file.')
    parser.add_argument('--vote_results_path', action = 'store', dest = 'vote_results_path', default='vote_results.csv', required = False, help = 'Filepath to vote_results csv file.')
    parser.add_argument('--output_path', action = 'store', dest = 'output_path', default='output.csv', required = False, help = 'Filepath to output csv file.')
    parser.add_argument('--deliver_mode', action = 'store', dest = 'deliver_mode', default='1', required = False, help = 'Deliverable mode. 1 or 2, based on the provided questions.')

    print("Parsing arguments.")
    args = parser.parse_args()
  except Exception as e:
    print("Error parsing the arguments: " + str(e))
    exit()

  print("Creating BillVisualizator object.")
  visualizator = BillVisualizator(args.bills_path, args.legislators_path, args.votes_path, args.vote_results_path)
  
  if args.deliver_mode == '1':
    visualizator.get_first_deliverable(args.output_path)
  elif args.deliver_mode == '2':
    visualizator.get_second_deliverable(args.output_path)
  else:
    print("Invalid deliverable mode.")

# TODO's:
# - Add documentation
# - Add logging
# - Create a README.md file
# - Add exception handling
# - Create tests
# - Check filepaths