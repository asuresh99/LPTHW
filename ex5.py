my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy" % my_weight)
print ("Actually, that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are really %s depending on the coffee" % my_teeth)

print ("If I add my %r, %r, and %r I get %r." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

inches = 12
print ("%d inches is %.2f centimeters" % (inches, inches * 2.54))
pounds = 10
print ("%d inches is %.2f centimeters" % (pounds, pounds * 0.453592))