class ProfileManager:
    profile_stats = {}  # func_uid: List[Stats]

    @classmethod
    def profile(cls, func):
        # 1. get function identifier
        # 2. create Stats() type
        # 3. save in profile_stats date

        # if error, raise the error rather than returning
        pass

    @classmethod
    def get_profile(cls, func):
        # 1. Get UID
        # 2. return profile_stats[uid]
        pass


class A:

    @ProfileManager.profile
    def function_1(self, a, b, c=1):
        return (a + b) / c


class B:

    @ProfileManager.profile
    def function_1(self, a, b, c=1):
        return (a + b) / c
