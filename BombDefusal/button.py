def button_module(color, text):
    if color.lower() == "blue" and text.lower() == "abort":
        bar_color = input("Hold the button. What color is the color strip? ")
        __holding_button(bar_color)
    if text.lower() == "detonate":
        condition = input("Is there more than one battery? ")
        if condition.lower() == "yes":
            return "\nPress and immediately release the button"
    if color.lower() == "white":
        condition = input("Is there a lit indicator with the label CAR? ")
        if condition.lower() == "yes":
            bar_color = input("Hold the button. What color is the color strip? ")
            __holding_button(bar_color)
    if color.lower() == "yellow":
        bar_color = input("Hold the button. What color is the color strip? ")
        __holding_button(bar_color)
    if color.lower() == "red" and text.lower() == "hold":
        return "\nPress and immediately release the button"
    else:
        condition = input("Are there more than 2 batteries? ")
        if condition.lower() == "yes":
            condition = input("Is there a lit indicator with the label FRK? ")
            if condition.lower() == "yes":
                return "Press and immediately release the button"
            else:
                __holding_button(None)


def __holding_button(color):
    if color.lower() == "blue":
        return "\nRelease the button when the countdown timer has 4 in any position"
    elif color.lower() == "white":
        return "\nRelease the button when the countdown timer has 1 in any position"
    elif color.lower() == "yellow":
        return "\nRelease the button when the countdown timer has 5 in any position"
    elif color == None:
        bar_color = input("Hold the button. What color is the color strip? ")
        __holding_button(bar_color)
    else:
        return "\nRelease the button when the countdown timer has 1 in any position"

