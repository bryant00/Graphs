import sys

sys.path.append("../graph")
from graph import Graph
from util import Stack, Queue, names
from random import sample


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    # try:
    #     avgerage = self.friendshipCount / self.userCount
    # except ZeroDivisionError:
    #     avgerage = 0

    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.userCount = 0
        self.friendshipCount = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            self.friendshipCount += 1

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        self.userCount += 1

    def populate_graph(self, num_users, avg_friendships):
        # import random
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # create 10 friends
        [self.add_user(i["first_name"]) for i in names[:num_users]]
        userIds = list(self.users.keys())
        for userId in userIds:
            print(userId)
            connections = sample(userIds, avg_friendships)
            for i in connections:
                self.add_friendship(userId, i)

        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
