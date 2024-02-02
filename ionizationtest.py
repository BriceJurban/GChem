from mendeleev import element

# Get the first ionization energy for the first 10 elements
for i in range(1, 11):
    ie_list = element(i)._ionization_energies
    if ie_list:
        print(ie_list[0])
    else:
        print(None)
