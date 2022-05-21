import random
import numpy as np


def code_challenge_one():
    vector_elements = []
    for i in range(0,20):
        vector_elements.append(random.randint(0,100))

    v1 = np.array([vector_elements[0],vector_elements[1],vector_elements[2],vector_elements[3],vector_elements[4],])
    v2 = np.array([vector_elements[5],vector_elements[6],vector_elements[7],vector_elements[8],vector_elements[9],])
    v3 = np.array([vector_elements[10],vector_elements[11],vector_elements[12],vector_elements[13],vector_elements[14]])
    v4 = np.array([vector_elements[15],vector_elements[16],vector_elements[17],vector_elements[18],vector_elements[19],])

    scalars = [random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)]

    result = scalars[0]*v1 + scalars[1]*v2 + scalars[2]*v3 + scalars[3]*v4
    return result


def code_challenge_two():
     vector = np.array([random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)])
     vector_dimensionality = len(vector)
     second_vector_elements = 1 / vector_dimensionality
     second_vector_list = []
     for element in vector:
         second_vector_list.append(second_vector_elements)
     second_vector = np.array(second_vector_list)
     dot_product = np.dot(vector, second_vector)
     return dot_product


def code_challenge_three():
    vector = np.array([random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)])
    second_vector = np.array([.5, .25, .125, .125])
    dot_product = np.dot(vector, second_vector)
    print(vector, dot_product)
    return dot_product

code_challenge_three()


