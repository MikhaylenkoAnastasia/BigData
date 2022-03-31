# cache function
def cache(times):
    def mind(func):
        def memory():
            memory.count += 1
            if memory.count == 1 or memory.count > times + 1:
                memory.x = func()
                memory.count = 1

            else:
                print(memory.x)


        memory.x = ''
        memory.count = 0
        return memory

    return mind


@cache(times=3)
def f():
    return input('? ')



