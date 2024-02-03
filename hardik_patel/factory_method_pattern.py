"""
Learn how to create simple factory which helps to hide logic of creating objects.
"""

from abc import ABCMeta, abstractmethod


class AbstractDegree(metaclass=ABCMeta):
    """Person representation"""
    @abstractmethod
    def info(self):
        pass


class BE(AbstractDegree):
    def info(self):
        print("Bachelor of Engineering")

    def __str__(self):
        return "Bachelor of Engineering"


class ME(AbstractDegree):
    def info(self):
        print("Master of Engineering")

    def __str__(self):
        return "Master of Engineering"


class MBA(AbstractDegree):
    def info(self):
        print("Master of Business Administration")

    def __str__(self):
        return "Master of Business Administration"


class ProfileAbstractFactory(object):
    def __init__(self):
        self._degrees = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def add_degree(self, degree):
        self._degrees.append(degree)

    def get_degrees(self):
        return self._degrees


class ManagerFactory(ProfileAbstractFactory):
    def create_profile(self):
        self.add_degree(MBA())
        self.add_degree(ME())


class EngineerFactory(ProfileAbstractFactory):
    def create_profile(self):
        self.add_degree(ME())
        self.add_degree(BE())


class ProfileCreatorFactory(object):
    @classmethod
    def create_profile(cls, name):
        return eval(profile_type + "Factory")()


if __name__ == "__main__":
    profile_type = input("Which profile would you like to create? [Manager/Engineer]: ")
    profile = ProfileCreatorFactory().create_profile(profile_type)
    print(f"Creating profile of {profile_type}")
    print("Profile has degrees: ")
    for degree in profile.get_degrees():
        print(f"-- {degree}")
