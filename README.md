Risk2210
========

Java clone of a modified-rules version of Risk 2210 that I play with my friends

actually, lets try python


Known issues:
Terminal output: [timestamp] Python[5166:1107] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
	First appeared after I added name input dialogue box, always printed to terminal after I exit the dialogue. I googled it, I think it is a bug in interfacing between Qt and the OS. does not affect application execution.





using example code from:
	zetcode.com/gui/pysidetutorial/
	stackoverflow.com/questions/2286864/how-can-i-add-a-picture-to-a-qwidget-in-pyqt4
	http://www.saltycrane.com/blog/2006/12/larger-python-qt-pyqt-example/ (QSpacerItem)