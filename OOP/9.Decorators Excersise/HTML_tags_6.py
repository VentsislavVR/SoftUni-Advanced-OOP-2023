def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper
    return decorator

# @tags('t')
@tags('p')
def join_strings(*args):
    return ''.join(args)
print(join_strings("Hello"," you!"))