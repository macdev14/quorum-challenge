import pandas as pd
import csv



class votes:

    bill_id = None
    vote_id = None

    def __init__(self, vote_results='vote_results.csv', votes='votes.csv', legislators='legislators.csv', 
    bills='bills.csv', first_task_file_name='legislators-support-oppose-count.csv', second_task_file_name='new_bills.csv') -> None:
        ''' 
        vote results CSV,
        votes CSV,
        legislators CSV,
        bills csv
        '''
        # order of n O(n)
        # length of csv file
        # omega of 1
        # store first output file name
        self.first_task_file_name = first_task_file_name
        # store second output file name
        self.second_task_file_name = second_task_file_name
        # Uses panda to read csv and calls iterrows()

        # reads vote result ensures delimiter
        self.vote_results = pd.read_csv(vote_results, delimiter= ',').iterrows()
        # reads votes ensures delimiter
        self.votes = pd.read_csv(votes, delimiter= ',').iterrows()
        # reads legislators ensures delimiter
        self.legislators = pd.read_csv(legislators, delimiter= ',').iterrows()
        # reads bills ensures delimiter
        self.bills = pd.read_csv(bills, delimiter= ',').iterrows()
        # reads vote result ensures delimiter again for second task
        self.vote_results_all = pd.read_csv(vote_results, delimiter= ',').iterrows()
        
        # calls function to invoke other two
        self.process_file()

    def process_file(self):
        
        # calls
        self.count_legislators_vote()
        self.count_bills_vote()
    
    def get_bill_id(self):
        # iterates through votes csv
        for i, row in self.votes:
            # check if vote id matched to what was defined earlier when called
            if row['id'] == self.vote_id:
                self.bill_id = row['bill_id']
            

   
    def count_legislators_vote(self):
        ''' Method to write to csv how many bills did the legislator support '''
        # create and open file
        with open(self.first_task_file_name, 'w') as file:
            # instance writer
            writer = csv.writer(file)
            # store header name in list
            header_support_oppose = ['id', 'name', 'num_supported_bills', 'num_opposed_bills']
            # write to csv
            writer.writerow(header_support_oppose)
            # declare support counter variable
            support = 0
            # declare legislator does not support counter variable
            not_support = 0
            # iterate legislators index and dictionary and write to csv
            for i, row_legislator in self.legislators:
                # iterate through result of votes
                for j, row in self.vote_results_all:
                    # check if legislator in vote results matches legislator in legislator.csv
                    if int(row['legislator_id']) == int(row_legislator['id']): 
                       # check and increment if supports
                        if int(row['vote_type']) == 1:
                            support = support + 1
                        # otherwise, check and increment if does not support    
                        elif int(row['vote_type']) == 2: not_support = not_support+ 1

                # predefined list structure to be written to csv
                data = [row_legislator['id'], row_legislator['name'], support, not_support ]
                # write to csv
                writer.writerow(data)
    
            
    
    def count_bills_vote(self):
        # create and open file
        with open(self.second_task_file_name, 'w') as file:
            # create writer instance
            writer = csv.writer(file)
            # store header name in list
            header_bills = ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor']
            # write to csv file
            writer.writerow(header_bills)
            # declare support counter variable
            support = 0
            # declare legislator does not support counter variable
            not_support = 0
            # loop index and key value based data structure (dictionaries)
            # iterate bills index and dictionary and write to csv
            for i, row_bills in self.bills:
                # iterate through result of votes
                for j, row in self.vote_results:
                    # needs bill id to check if it is a new voting bill 
                    if not self.bill_id or self.vote_id!=row['vote_id']:
                        # store vote_id which will be used by method get_bill_id()
                        self.vote_id = row['vote_id']
                        # call get_bill_id() which by getting vote id will be possible to get bill id
                        self.get_bill_id()
                    # otherwise bill_id is set and equals to current bills.csv id
                    if int(self.bill_id) == int(row_bills['id']): 
                        # check if is supported and increment
                        if int(row['vote_type']) == 1: support += 1
                        # check if it is not supported and increment
                        elif int(row['vote_type']) == 2: not_support+=1
                # predefined list structure to be written to csv
                data = [row_bills['id'], row_bills['title'], support, not_support, row_bills['sponsor_id'] ]
                # write to csv
                writer.writerow(data)

            
                    
            
            
        
    







