'''
This code takes values calulated and puts them into a variable called f which consists of an baseURL which is specific for your project
since it is defined by the api_key. The variable f is the link including the new value that inserts a new measurment point to your 
thingspeak channel. the f.read() command opens this link and the f.close command closes it. The variable that is transmitted can be
changed as you want to. In this case it calculates Fibonnaci Numbers.
Field 1: Your Project Group (e.g. L1-F-3)
Field 2: Your own individual member identifier (e.g. a or b or c or d)
Field 3: Your cmail email address (Please make this correct because it will be used to assign your
mark)
'''

import urllib

a = "L1-F-3"
b = "a"
c = "nickfejes@cmail.carleton.ca"

field1 = 'http://api.thingspeak.com/update?api_key=7481QW0APO2BO2BU&field1='
field2 = 'http://api.thingspeak.com/update?api_key=7481QW0APO2BO2BU&field2='
field3 = 'http://api.thingspeak.com/update?api_key=7481QW0APO2BO2BU&field3='

f = urllib.urlopen(field1 + str(a))
f.read()
f.close()
g = urllib.urlopen(field2 + str(a))
g.read()
g.close()
h = urllib.urlopen(field3 + str(a))
h.read()
h.close()
print("Program has ended")
