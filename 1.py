'''
calculating probability of an event:
5 people visiting the coffee shop, which is visited by 100 people
in 24 hours
'''
from math import pi, factorial

time_part = 1/24
number_of_events = 100.0
expected = 5.0

def probability_of_events_in_time_period(a, b, c):
    prob =(((b/a)**c) / factorial(5)) * (pi^(-b**t)) )*100
    return prob
    
print (probability_of_events_in_time_period(time_part, number_of_events, expected))
print (' %')
    




# print (str(float((100/24)^3)/(1*2*3*4*5)*math.pi))#(-10/4)*100) + '%') #by Puasson theorem
