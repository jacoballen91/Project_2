
class User:
    def __init__(self) -> None:
        """
        Method to initialize base values for Users
        """
        self.voters = []
        self.admin = 'admin123'
        self.admin_password = 'admin123'

    def voter(self, voter_id: str) -> bool:
        """
        Method to check that voter ID's are valid and haven't already voted, and to test for admin status
        :param voter_id: 8 digit numeric voter ID
        :return: boolean value indicating whether an admin ID was entered
        """
        if voter_id != self.admin:
            if voter_id.isdigit():
                if len(voter_id) == 8:
                    if voter_id in self.voters:
                        raise NameError
                    else:
                        self.voters.append(voter_id)
                        return False
                else:
                    raise TypeError
            else:
                raise ValueError
        else:
            return True

    def check_admin(self, password: str) -> bool:
        """
        Check validity of admin password
        :param password: entered password
        :return: Boolean value indicating whether the entered password matches the admin password
        """
        if password == self.admin_password:
            return True
        else:
            return False

