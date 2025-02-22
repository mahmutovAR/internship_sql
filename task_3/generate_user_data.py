from faker import Faker


class GeneratedUserData:
    """Class for generating test user data."""
    def __init__(self):
        self.fake = Faker()

    def generate_first_name(self) -> str:
        """Returns generated First Name."""
        return self.fake.first_name()

    def generate_last_name(self) -> str:
        """Returns generated Last Name."""
        return self.fake.last_name()

    def generate_full_name(self) -> tuple:
        """Returns generated Full Name."""
        return self.generate_first_name(), self.generate_last_name()
