class Friendship:
    friendship_id: int = None
    user1_id: int = None
    user2_id: int = None

    def __init__(self, friendship_id: int, user1_id: int, user2_id: int):
        self.friendship_id = friendship_id
        self.user1_id = user1_id
        self.user2_id = user2_id
