def fsa(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 2
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 2
            else:
                state = 0

    if state == 2:
        return "Accepted"
    else:
        return "Rejected"


string = input("Enter a string: ")
print("Result:", fsa(string))
