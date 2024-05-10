import csv
"""
Create voting.csv and header
"""
with open('voting.csv', 'w', newline='') as output_csv:
    contents = csv.writer(output_csv)
    contents.writerow(['Candidate', 'Number of Votes'])


class Voting:
    def __init__(self) -> None:
        """
        Initializes base values for Voting
        """
        self.candidates = {'Jack': 0, 'Jill': 0}
        self.candidate_list = ['Jack', 'Jill']

    def update_csv(self) -> None:
        """
        Method to update voting.csv anytime data is updated, using a dictionary
        """
        csv_file = 'voting.csv'
        with open(csv_file, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Candidate', 'Number of Votes'])
            for key, value in self.candidates.items():
                csv_writer.writerow([key, value])

    def add_vote(self, name: str) -> None:
        """
        Method to increase votes for candidates
        :param name: candidate name
        """
        if name in self.candidates.keys():
            num_votes = self.candidates[name]
            num_votes += 1
            self.candidates.update({name: num_votes})
            self.update_csv()
        else:
            raise NameError

    def add_candidate(self, name: str) -> None:
        """
        Method to add new candidates to the voting options
        Includes data validation to ensure minimum length and that entry doesn't exist
        :param name: candidate name
        """
        if len(name) > 0 and name not in self.candidates.keys():
            self.candidates.update({name:  0})
            self.candidate_list.append(name)
            self.update_csv()
        elif len(name) <= 0:
            raise ValueError
        elif name in self.candidates.keys():
            raise NameError

    def __str__(self) -> str:
        """
        Method to calculate votes and return voting information
        :return: Voting results
        """
        total_votes = 0
        temp_result = ''
        high_votes = 0
        winner = ''
        result = ''
        for key, value in self.candidates.items():
            if value > total_votes:
                high_votes = value
                winner = key
            total_votes += value
            temp_result += key + ': ' + str(value) + '\n'
        if total_votes > 0:
            result += f'Congratulations, {winner}! {winner} won with {high_votes} votes!\n'
        result += f'A total of {total_votes} votes were cast\n'
        result += temp_result
        return result


