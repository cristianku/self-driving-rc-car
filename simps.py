import  scipy.integrate  as integrate

y = [100,200,300, 400, 500, 300, 400,300,200,100,200,100]
dt = 0.0001
velocity = integrate.simps(y, dx=dt)

print " velocity = ", velocity