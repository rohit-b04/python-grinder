class MyError(Exception):
    pass


def check_error(user_input):
    try:
        if not user_input.isdigit():
            raise MyError("Not a number!")
    except Exception as e:
        print(e)
        return True
    return False
