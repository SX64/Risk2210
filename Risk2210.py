#!/usr/bin/env python

#need to figure out QT

#need to copy over what I have with java

#need more cowbell

#ideas that need to be implemented: //in no particular order
#space station
#commanders (is a guy)
#borders
#territories
#guys
#commander types
#player
#turn
#turn order
#the moon
#regions, for lack of the correct term
#bonuses (technically boni)
#cards
#card types
#energy
#dice
#an attack
#contiguity
#eight sided dice
#water vs land vs moon territories
#territory ownership
#contiguity
#


#pyside test

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Simple')
wid.show()

sys.exit(app.exec_())