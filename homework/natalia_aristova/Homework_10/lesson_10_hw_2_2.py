def repeat_me1(count):

    def my_func(func):

        def wrapper(text):
            for i in range(count):
                func(text)
        return wrapper
    return my_func


@repeat_me1(count=2)
def example(text):
    print(text)


example('print me')
