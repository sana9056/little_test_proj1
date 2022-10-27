class Animal(object):
    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

    def get_voice(self):
        """
        What does it say?
        """
        say = "It's says %s" % (self.voice)
        return say

    def get_info(self):
        """
        Who are you?
        """
        return "%s is %s. It's says %s." % (self.name, self.color, self.voice)


if __name__ == "__main__":
    cat = Animal("Cat", "black", "Meow")
    cow = Animal("Cow", "purple", "MOOOOOOOO")
    dog = Animal("Dog", "orange", "Wof-Wof")
    print(cat.get_info())
    print(cow.get_info())
    print(dog.get_info())
