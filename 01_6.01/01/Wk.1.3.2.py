#
#  MIT 6.01 (Week 1)
#  Design Lab 1. Problem 1.3.2
#
#  Created by Dulio Denis on 1/4/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_1_3_2.pdf
#
class Car:
 color = 'gray'
 def describeCar(self):
	return 'A cool ' + Car.color + ' car'
 def describeSelf(self):
	return 'A cool ' + self.color + ' car'

nona = Car()
print "1. nona.describeCar() yields: %s" % nona.describeCar()
print "2. nona.describeSelf() yields: %s" %  nona.describeSelf()
print "3. nona.color yields: %s" % nona.color

lola = Car()
lola.color = 'plaid'
 

print "4. lola.describeCar() yields: %s" % lola.describeCar()
print "5. lola.describeSelf() yields: %s" %  lola.describeSelf()
print "6. lola.color yields: %s" % lola.color 
print "7. nona.describeSelf() yields: %s" %  nona.describeSelf() 

nona.size = 'small'

# print "8. lola.size yields: %s" % lola.size
print "8. lola.size yields: %s" % "AttributeError: Car instance has no attribute 'size'"

Car.size = 'big'

print "9. lola.size yields: %s" % lola.size 
print "10. nona.size yields: %s" % nona.size 