import sys

sys.path.append("../graph")
from graph import Graph
from util import Stack, Queue, names
from random import sample


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
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
        totalFriends = num_users * avg_friendships
        # create 10 friends
        [self.add_user(i["first_name"]) for i in names[:num_users]]
        userIds = list(self.users.keys())
        addedFriendships = {}
        # while self.friendshipCount < 21:
        # for i in range(totalFriends):
        #     for j in range(totalFriends):
        while True:
            if self.friendshipCount == totalFriends:
                break
                # self.add_friendship(userIds[i], sample(userIds, 1)[0])
            friend1 = sample(userIds, 1)[0]
            friend2 = sample(userIds, 1)[0]
            # self.add_friendship(sample(userIds, 1)[0], sample(userIds, 1)[0])
            self.add_friendship(friend1, friend2)
            friends = [friend1, friend2]
            # print("addFriendship", friends)
            # print("friendshipCount", self.friendshipCount)
            # friends.sort()
            addedFriendships[friends[0]] = friends[1]
            k = friends[0]
            v = friends[1]
        # print("addedFriendships: ", addedFriendships)

        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = {}
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited.keys():
                if vertex == destination_vertex:
                    return path
                visited[vertex] = self.users[vertex]
                for next_vert in self.friendships[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # depth first traversal
        stack = Stack()
        stack.push(user_id)
        visited = {}
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited.keys():
                # print(vertex)
                # visited[vertex] = self.users[vertex]
                visited[vertex] = self.bfs(user_id, vertex)
                for next_vert in self.friendships[vertex]:
                    stack.push(next_vert)

        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(15, 2)
    print("friendships: ", sg.friendships)
    user = 15
    connections = sg.get_all_social_paths(user)
    print("user ", user, "connections: ", connections)
    # sg.bfs(1, 9)

    # print("friendshipCount:", sg.friendshipCount)
