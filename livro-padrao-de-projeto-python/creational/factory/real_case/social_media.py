from abc import ABC, abstractmethod


class Section(ABC):
    @abstractmethod
    def describe(self): pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(ABC):
    def __init__(self):
        self.__sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.__sections

    def add_section(self, section):
        self.__sections.append(section)


class Linkedin(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    profile_type = input('Which profile you would like to create ? [Linkedin, Facebook]')
    profile = eval(profile_type)()
    print("Creating profile ..", type(profile).__name__)
    print("Profile has sections ..", profile.get_sections())
