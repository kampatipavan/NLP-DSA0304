def fsa(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'c':
                state = 3
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 3:
            if ch == 'a':
                state = 1
            else:
                state = 0

    if state == 3:
        return "Accepted"
    else:
        return "Rejected"


string = input("Enter a string: ")
print("Result:", fsa(string))
