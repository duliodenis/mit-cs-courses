#
#  MIT 6.01 (Week 1)
#  Design Lab 1. Problem 1.3.1
#
#  Created by Dulio Denis on 1/4/15.
#  Copyright (c) 2015 ddApps. All rights reserved.
# ------------------------------------------------
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/object-oriented-programming/MIT6_01SCS11_designLab01.pdf
#
# Objective: Write the definition of a Python procedure fib, such that fib(n) returns
# the nth Fibonacci number.
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


# Test the Fibonacci procedure
firstTest = 6  # fib(6) -> 8
secondTest = 7 # fib(7) -> 13
thirdTest = 8  # fib(8) -> 21
firstResult = fib(firstTest)
secondResult = fib(secondTest)
thirdResult = fib(thirdTest)

print "fib1(%r) = %r" % (firstTest, firstResult)
print "fib2(%r) = %r" % (secondTest, secondResult)
print "fib3(%r) = %r" % (thirdTest, thirdResult)