def wire_module(num_wires):
    if num_wires == 3:
        condition = input("Are there red wires? ")
        if condition.lower() == "no":
            return "\nCut the second wire"
        condition = input("Is the last wire white? ")
        if condition.lower() == "yes":
            return "\nCut the last wire"
        condition = input("Is there more than one blue wire? ")
        if condition.lower() == "yes":
            return "\nCut the last blue wire"
        else:
            return "\nCut the last wire"
    if num_wires == 4:
        condition = input("Is there more than one red wire? ")
        if condition.lower() == "yes":
            condition = input("Is the last digit of the serial number odd? ")
            if condition.lower() == "yes":
                return "\nCut the last red wire"
        condition = input("Is last wire yellow? ")
        if condition.lower() == "yes":
            condition = input("Are there any red wires? ")
            if condition.lower() == "no":
                return "\nCut the first wire"
        condition = input("Is there one blue wire? ")
        if condition.lower() == "yes":
            return "\nCut the first wire"
        condition = input("Is there more than one yellow wire? ")
        if condition.lower() == "yes":
            return "\nCut the last wire"
        else:
            return "\nCut the second wire"
    if num_wires == 5:
        condition = input("Is the last wire black? ")
        if condition.lower() == "yes":
            condition = input("Is the last digit of the serial number odd? ")
            if condition.lower() == "yes":
                return "\nCut the fourth wire"
        condition = input("Is there one red wire? ")
        if condition.lower() == "yes":
            condition = input("Is there more than one yellow wire? ")
            if condition.lower() == "yes":
                return "\nCut the first wire"
        condition = input("Are there any black wires? ")
        if condition.lower() == "no":
            return "\nCut the second wire"
        else:
            return "\nCut the first wire"
    if num_wires == 6:
        condition = input("Are there any yellow wires? ")
        if condition.lower() == "no":
            condition = input("Is the last digit of the serial number odd? ")
            if condition.lower() == "yes":
                return "\nCut the third wire"
        condition = input("Is there one yellow wire? ")
        if condition.lower() == "yes":
            condition = input("Is there more than white wire? ")
            if condition.lower() == "yes":
                return "\nCut the fourth wire"
        condition = input("Are there any red wires? ")
        if condition.lower() == "no":
            return "\nCut the last wire"
        else:
            return "\nCut the fourth wire"
