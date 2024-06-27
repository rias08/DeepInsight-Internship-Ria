#Codecademy
print("Hello world!")

#futurecoder
print(1+2)
print(1/2)
print(2/1)
print(1*2)
print((1+2)*(2/1*2/1/2))

print("Hello" + " World!")
print("Hello" + " " + "World!")

word = "Hello"
your_name = "Ria"
print(word + " " + your_name)
sentence = word + " " + your_name
print(sentence)

name = "World"
line = ""
for char in name:
    line = line + char
    print(line)

for char in name:
    line += "-"
print(name)
print(line)

print(1+1)

#Displaying sum of pollution of each country (Argonne coding camp)
Pollution_Data = {'China': [1448.46, 1439.86, 1506.94, 1593.39, 1724.49, 1857.81, 1970.82, 2102.78, 2240.37, 2275.34, 2269.71, 2369.25, 2449.16, 2626.64, 2831.55, 2861.68, 2893.38, 3081.74, 2967.26, 2885.72, 2849.75, 2969.58, 3464.84, 4069.24, 5089.78, 5512.70, 5817.14, 6184.10, 6721.43, 7204.89, 8320.96],
'United_States': [4776.83, 4647.13, 4411.29, 4388.21, 4618.54, 4604.61, 4612.50, 4769.99, 4989.71, 5069.96, 5040.59, 4997.43, 5093.61, 5188.45, 5261.19, 5319.78, 5505.92, 5578.55, 5616.57, 5676.70, 5861.32, 5753.71, 5799.04, 5850.98, 5969.03, 5991.76, 5914.50, 6015.75, 5835.38, 5427.07, 5610.11],
'India': [291.23, 337.78, 349.74, 367.40, 421.91, 447.38, 473.74, 486.59, 522.28, 553.48, 578.62, 620.85, 659.37, 690.76, 733.91, 870.23, 827.81, 870.04, 906.33, 962.30, 1002.95, 1025.68, 1015.84, 1032.07, 1125.84, 1183.28, 1282.68, 1368.38, 1474.20, 1622.70, 1695.62],
'Japan': [947.01, 945.01, 899.79, 867.13, 935.74, 926.25, 877.53, 890.40, 959.77, 989.37, 1046.98, 1066.42, 1073.47, 1064.34, 1118.44, 1116.24, 1134.96, 1157.75, 1113.11, 1156.38, 1201.43, 1193.69, 1199.95, 1249.72, 1256.26, 1241.26, 1239.89, 1254.44, 1215.48, 1104.60, 1164.47]}

sum = 0
for items in Pollution_Data:
  for data in Pollution_Data[items]:
    sum = sum + data
  print(f'The total pollution in {items} is {sum}.')


#Finding weight of each molecule (Argonne coding camp)

atom_weights = {'H': 1.008, 'He': 4.003, 'Li': 6.938, 'Be': 9.012, 'B': 10.806, 'C':12.010, 'N': 14.006,
                'O': 15.999, 'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.304, 'S': 32.059, 'Cl': 35.446}


molecules = {'water': ['H', 'H', 'O'],
             'carbon dioxide': ['C', 'O', 'O'],
             'sodium chloride': ['Na', 'Cl'],
             'magnesium sulfide': ['Mg', 'S'],
             'glucose': ['C', 'C', 'C', 'C', 'C', 'C',
                         'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H',
                         'O', 'O', 'O', 'O', 'O', 'O']}

for atoms in molecules:
   sum = 0
   for weights in molecules[atoms]:
      sum = sum + atom_weights[weights] 
   print(sum)