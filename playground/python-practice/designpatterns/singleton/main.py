class Singleton:
    _instance = None  # class level attribute

    def __new__(cls, *args, **kwargs):  # override new method
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(f"singleton1 ID: {id(singleton1)}")
    print(f"singleton2 ID: {id(singleton2)}")

    if singleton1 is singleton2:
        print("Both are the same instance (Singleton is working correctly).")
    else:
        print("Different instances (Singleton failed).")
