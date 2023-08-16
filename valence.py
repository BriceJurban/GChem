# Define the valence electrons for the elements.
VALENCE_ELECTRONS = {
    'H': 1,
    'He': 2,
    'Li': 1,
    'Be': 2,
    'B': 3,
    'C': 4,
    'N': 5,
    'O': 6,
    'F': 7,
    'Ne': 8,
    'Na': 1,   # Sodium
    'Mg': 2,   # Magnesium
    'Al': 3,   # Aluminum
    'Si': 4,   # Silicon
    'P': 5,    # Phosphorus
    'S': 6,    # Sulfur
    'Cl': 7,   # Chlorine
    'Ar': 8,   # Argon
}

def get_valence_electrons(formula):
    total_valence = 0
    element = ""
    number = ""
    i = 0
    
    while i < len(formula):
        char = formula[i]

        if char == '(':
            # Find the corresponding closing parenthesis
            depth = 1
            start = i + 1
            while i < len(formula) and depth != 0:
                i += 1
                if formula[i] == '(':
                    depth += 1
                elif formula[i] == ')':
                    depth -= 1
            
            # Recurse into the subformula inside the parenthesis
            multiplier = ""
            while (i + 1 < len(formula)) and formula[i + 1].isdigit():
                i += 1
                multiplier += formula[i]

            total_valence += get_valence_electrons(formula[start:i]) * (int(multiplier) if multiplier else 1)

        else:
            # If character is a letter, we're reading an element symbol
            if char.isalpha():
                # If it's a capital letter, it's the start of a new element symbol
                if char.isupper():
                    # If we had been reading an element, add its valence electrons
                    if element:
                        total_valence += VALENCE_ELECTRONS[element] * (int(number) if number else 1)
                    # Start reading new element
                    element, number = char, ""
                else:
                    # If it's a lowercase letter, it's the continuation of an element symbol
                    element += char

            # If character is a number, it indicates the number of that element
            elif char.isdigit():
                number += char

        i += 1

    # Account for the last element read, if there was one
    if element:
        total_valence += VALENCE_ELECTRONS[element] * (int(number) if number else 1)

    return total_valence

def main():
    while True:
        formula = input("Enter the chemical formula: ")
        if formula.lower() == 'exit':
            break
        try:
            print("The number of valence electrons in {} is: {}".format(formula, get_valence_electrons(formula)))
        except KeyError:
            print("Invalid element in formula or element not in the database.")
        print()  # for spacing

main()