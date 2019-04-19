from functools import wraps


def input_required(func):
    """
    Decorator for require the input class methods.
    must have attribute "name" and "has_input".
    Usages:
        @input_required
        def get_output(self):
            pass
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.has_input:
            raise Exception("{} must have input pin(s)!".format(str(self.name)))

        return func(self, *args, **kwargs)

    return wrapper
