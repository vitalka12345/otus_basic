# decorator
def header(func):
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")

    return inner


def table(func):
    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")

    return inner


@header
@table  # say = header(table(say))
def say(name, surname, age):
    print("hello", name, surname, age)


say("Ivan", "Petrov", 45)
