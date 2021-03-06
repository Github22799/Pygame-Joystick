import os

try:
    import pygame
except ModuleNotFoundError:
    import pip

    pip.main(['install', 'pygame'])
finally:
    import pygame

pygame.init()
pygame.joystick.init()


class Joystick:

    # Do remember to call the "refresh" method before asking for values.

    @staticmethod
    def joystick_count():
        return pygame.joystick.get_count()

    def __init__(self, joystick_num=0):
        self.joystick = pygame.joystick.Joystick(joystick_num)
        self.joystick.init()

    def get_joystick(self):
        return self.joystick

    def id(self):
        try:
            jid = self.joystick.get_instance_id()
        except AttributeError:
            jid = self.joystick.get_id()
        return jid

    def name(self):
        return self.joystick.get_name()

    def guid(self):
        try:
            guid = self.joystick.get_guid()
        except AttributeError:
            guid = None

        return guid

    def axis_count(self):
        return self.joystick.get_numaxes()

    def axis_value(self, i):
        return self.joystick.get_axis(i)

    def buttons_count(self):
        return self.joystick.get_numbuttons()

    def button_value(self, i):
        return self.joystick.get_button(i)

    def hats_count(self):
        return self.joystick.get_numhats()

    def hat_value(self, i):
        return self.joystick.get_hat(i)

    @staticmethod
    def refresh():
        pygame.event.pump()


class JoystickInfo:

    # helper class for printing information about a given joystick

    def __init__(self, joystick):
        self.joystick = joystick

    def id(self):
        jid = self.joystick.id()
        return f"Joystick {jid}:"

    def name(self):
        name = self.joystick.name()
        return f"Joystick name: {name}"

    def guid(self):
        guid = self.joystick.guid()
        if guid:
            return f"GUID: {guid}"
        return None

    def axis(self):
        res = ''
        axes_count = self.joystick.axis_count()
        res += f"Number of axes: {axes_count}" + '\n'

        for i in range(axes_count):
            axis = self.joystick.axis_value(i)
            res += "Axis {} value: {:>6.3f}".format(i, axis) + '\n'

        return res

    def buttons(self):
        res = ''
        buttons_count = self.joystick.buttons_count()
        res += f"Number of buttons: {buttons_count}" + '\n'

        for i in range(buttons_count):
            button = self.joystick.button_value(i)
            res += "Button {:>2} value: {}".format(i, button) + '\n'

        return res

    def hats(self):
        res = ''
        hats_count = self.joystick.hats_count()
        res += f"Number of hats: {hats_count}" + '\n'

        for i in range(hats_count):
            hat = self.joystick.hat_value(i)
            res += f"Hat {i} value: {hat}" + '\n'

        return res

    def all_info(self):
        res = ''
        res += self.id() + '\n'
        res += self.name() + '\n'
        guid = self.guid() + '\n'
        if guid:
            res += guid + '\n'
        res += self.axis() + '\n'
        res += self.buttons() + '\n'
        res += self.hats() + '\n'
        self.joystick.refresh()

        return res


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_to_file(filename, string):
    file = open(filename, 'w')
    file.write(string)
    file.close()


def main(fps=60):

    clock = pygame.time.Clock()

    while True:
        cls()
        joystick = Joystick()
        joystick_info = JoystickInfo(joystick)
        info = joystick_info.all_info()
        save_to_file('info.txt', info)
        print(info)
        clock.tick(fps)


main(20)
