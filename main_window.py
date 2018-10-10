#!/usr/bin/python3
import toga
import os

from toga.style import Pack
from random import randrange

# local lib

class DND(toga.App):
    def startup(self):

        # Create main window
        self.main_window = toga.MainWindow(self.name)
        icons = os.path.join(os.path.dirname(__file__), 'icons')

        # dice number window
        self.roll_dice = ''
        self.die_window = toga.Window('die_num', title='How many dice to roll', closeable=False,
                                      minimizable=False)
        self.dice_number = toga.Slider(range=(1,10), window=self.die_window)


        # Character Attributes on the left
        self.left_content = toga.Slider()
        self.left_container = toga.ScrollContainer(content=self.left_content, horizontal=False)

        # Other attributes on the right
        self.right_container = toga.OptionContainer()

        self.right_table = toga.Table(headings=['Throws', 'Values'])
        self.right_tree = toga.Tree(headings=['Spells', 'Equipment'])

        self.right_container.add('Table', self.right_table)
        self.right_container.add('Tree', self.right_tree)


        # Split left and right boxes formed above
        self.split = toga.SplitContainer()
        self.split.content = [self.left_container, self.right_container]

        # Make dice toolbar
        cmd4 = toga.Command(self.dice4,
                            'Roll D4',
                            tooltip='Roll a four sided die',
                            icon=os.path.join(icons, 'd4.png'),
                            order=1)
        cmd6 = toga.Command(self.dice6,
                            'Roll D6',
                            tooltip='Roll a six sided die',
                            icon=os.path.join(icons, 'd6.png'),
                            order=2)
        cmd8 = toga.Command(self.dice8,
                            'Roll D8',
                            tooltip='Roll a eight sided die',
                            icon=os.path.join(icons, 'd8.png'),
                            order=3)
        cmd10 = toga.Command(self.dice10,
                            'Roll D10',
                            tooltip='Roll a 10 sided die',
                            icon=os.path.join(icons, 'd10.png'),
                            order=4)
        cmd12 = toga.Command(self.dice12,
                            'Roll D12',
                            tooltip='Roll a twelve sided die',
                            icon=os.path.join(icons, 'd12.png'),
                            order=5)
        cmd20 = toga.Command(self.dice20,
                            'Roll D20',
                            tooltip='Roll a twenty sided die',
                            icon=os.path.join(icons, 'd20.png'),
                            order=6)

        # Show main window
        self.main_window.toolbar.add(cmd4, cmd6, cmd8, cmd10, cmd12, cmd20)
        self.main_window.toolbar.add(die_slider)
        self.main_window.content = self.split
        self.main_window.show()

    # Die number selection window
    def die_window(self, widget):
        self.

    # Make the dice roll actions
    def dice4(self, widget):
        self.main_window.info_dialog('D4 Roll', str(randrange(1,4)))
    def dice6(self, widget):
        self.main_window.info_dialog('D6 Roll', str(randrange(1,6)))
    def dice8(self, widget):
        self.main_window.info_dialog('D8 Roll', str(randrange(1,8)))
    def dice10(self, widget):
        self.main_window.info_dialog('D10 Roll', str(randrange(1,10)))
    def dice12(self, widget):
        self.main_window.info_dialog('D12 Roll', str(randrange(1,12)))
    def dice20(self, widget):
        self.main_window.info_dialog('D20 Roll', str(randrange(1,20)))


if __name__ == '__main__':
    dnd_app = DND('DND App', 'pilith.com.dnd')
    #dnd_app.startup()
    dnd_app.main_loop()