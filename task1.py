import math
import numpy as np
import matplotlib.pyplot as plt 


A = np.linspace(0, 5, 100)

def p():
    return A * np.exp(-A)

plt.plot(A, p()) 

plt.xlabel("A=λh")
plt.ylabel("p(1)")
plt.title("Probability of correct transmission")
plt.grid()

plt.show()
