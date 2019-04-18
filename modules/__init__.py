from functools import wraps

def input_required(func):
    """
    Required input
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.has_input:
            raise Exception("{} must have input pin(s)!".format(self.name))
            
        return func(self, *args, **kwargs)

    return wrapper
