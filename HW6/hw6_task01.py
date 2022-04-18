def instances_counter(cls):
    cls.count = 0
    class Wrapper(cls):
        def init(self):
            cls.count += 1

        @classmethod
        def get_created_instances(cls):
            print("Total objects: ", Wrapper.count)

        @classmethod
        def reset_instances_counter(cls):
            cls.counter = 0
            print("Counter is 0")

    return Wrapper


@instances_counter
class User:
    pass


if name == 'main':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  #3