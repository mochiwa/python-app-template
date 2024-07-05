from infrastructure.Container import Container


def init_container():
    c = Container()
    c.register("1", "Hello")
    c.register(str, lambda x: print(c.get_service("1")))
    return c
