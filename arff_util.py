import re
import math

def get_first(list):
    return list[0] if len(list) > 0 else 0

textfile = open('contact-lenses.arff', 'r')
reg = re.compile(r'^[^\@\%].+$')
matches = []

for line in textfile:
    matches += reg.findall(line)

textfile.close()

for i in range(0, len(matches)):
    matches[i] = matches[i].split(',')

number_of_lines = len(matches)

for i in range(0, len(get_first(matches)) - 1):
    values = {}
    count = 0
    for j in range(0, len(matches)):
        attribute = matches[j][i]
        class_attribute = matches[j][len(get_first(matches)) - 1]
        if attribute in values.keys():
            if class_attribute in values[attribute].keys():
                values[attribute][class_attribute] += 1
            else:
                values[attribute][class_attribute] = 1

        else:
            values[attribute] = {}
            values[attribute][class_attribute] = 1

    expected_value = 0
    for key in values:
        entropy_sum = 0
        denomenator = sum(values[key].values())
        for class_attribute in values[key]:
                    
            constant = float(values[key][class_attribute]) / denomenator
            if constant != 0:
                entropy_sum += -1 * constant * math.log(constant, 2)

        expected_value += entropy_sum * (float(denomenator) / number_of_lines)

    print("The expected value of " +key +" is " +str(expected_value))
