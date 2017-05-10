class ExceptionClass(Exception):
    pass

object_exception = ExceptionClass()

raise ExceptionClass('Something is wrong')