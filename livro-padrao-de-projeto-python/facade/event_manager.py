class Hotelier:

    def __init__(self):
        print("Arranging the Hotel for Marriage ? ")

    def book_hotel(self):
        if self.__is_available():
            print("Registered the Booking\n\n")

    @staticmethod
    def __is_available():
        print("Is the Hotel available?")
        return True


class Florist:

    def __init__(self):
        print("Flower decoration for the event ? ")

    def set_flower_requirements(self):
        print("Carnation, roses and Lilies would be used for decorations\n\n")


class Caterer:

    def __init__(self):
        print("Food arrangement for the event ? ")

    def set_cuisine(self):
        print("Chinese & Continental Cuisines would be serverd\n\n")


class Musician:

    def __init__(self):
        print("Musician arrangement for the event ? ")

    def set_music_type(self):
        print("Jazz and classical will be played\n\n")


class EventManager:
    def __init__(self):
        print("Event Manager :: Let me talk to the folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class You:
    def __init__(self):
        print("You :: Whoa! Marriage Arrangements ?? ")

    def ask_event_manager(self):
        print("You :: Let's Contact the event manager ")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You :: Thanks to Event Manager, all preparations done! Phew!")


if __name__ == '__main__':
    you = You()
    you.ask_event_manager()
