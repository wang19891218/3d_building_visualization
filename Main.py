import os
import numpy
import scipy
from scipy.misc import factorial
from matplotlib import pyplot

Array_Phase = numpy.linspace(0, 2 * numpy.pi, 1001)
Array_Target_Cos = numpy.cos(Array_Phase)
Array_Target_Sin = numpy.sin(Array_Phase)

for Value_Maximum_Interation in range(12):
    Array_Simulation_Cos = numpy.zeros(Array_Target_Cos.shape)
    Array_Simulation_Sin = numpy.zeros(Array_Target_Sin.shape)
    for i_Iteration in range(Value_Maximum_Interation):
        Array_Simulation_Cos += Array_Phase**(2 * i_Iteration) / factorial(2 * i_Iteration) * (-1)**(i_Iteration)
        Array_Simulation_Sin += Array_Phase**(2 * i_Iteration + 1) / factorial(2 * i_Iteration + 1) * (-1)**(i_Iteration)

    pyplot.plot(Array_Phase, Array_Target_Cos)
    pyplot.plot(Array_Phase, Array_Simulation_Cos)
    pyplot.plot(Array_Phase, Array_Target_Sin)

    pyplot.plot(Array_Phase, Array_Simulation_Sin)
    pyplot.axis([0, 2* numpy.pi, -1 ,1])
    pyplot.title(str(Value_Maximum_Interation))
    pyplot.show()


# This line is a test for the github
# Test 1
# Test 2
