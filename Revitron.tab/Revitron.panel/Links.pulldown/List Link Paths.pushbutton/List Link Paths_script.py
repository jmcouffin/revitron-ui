import revitron
from rpw.ui.forms import TextInput
from rpw.ui.forms import select_file

__context__ = 'zerodoc'

host = select_file('Revit Model (*.rvt)|*.rvt')
revitron.TransmissionData(host).listLinks()

print('Done')