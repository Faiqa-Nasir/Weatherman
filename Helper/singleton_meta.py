from abc import ABCMeta


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonABCMeta(ABCMeta, SingletonMeta):
    """A metaclass that combines Singleton behavior with Abstract Base Class (ABC) behavior."""
    pass
