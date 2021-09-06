class Maybe(object):

    def __init__(self, value):
        self.value = value

    @classmethod
    def unit(cls, value):
        return cls(value)

    def map(self, f):
        if self.value is None:
            return self  # forward the empty box
        new_value = f(self.value)
        return Maybe.unit(new_value)


def first_value(values):
    if len(values) > 0:
        return values[0]
    return None


class User:
    def __init__(self, name: str, friends: []):
        self.name = name
        self.friends: [User] = friends


class Request:
    def __init__(self, user: User):
        self.user = user


if __name__ == '__main__':
    me = User("Igli", None)
    gosha = User("Gosha", None)
    kimbo = User("Kimbo", None)
    sogga = User("Sogga", [me, gosha])
    floppa = User("Gosha Kerr", [sogga, kimbo])
    request = Request(user=floppa)
    friends_of_first_friends = (
        Maybe.unit(request)
        .map(lambda request: request.user)
        .map(lambda user: user.friends)
        .map(lambda friends: friends[0] if len(friends) > 0 else None)
        .map(lambda first_friend: first_friend.friends)
    )
    print(list(map(lambda user: user.name, friends_of_first_friends.value)))
