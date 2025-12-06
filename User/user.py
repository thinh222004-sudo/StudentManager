class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def show_info(self):
        print(f"User ID: {self.user_id} - Name: {self.name}")