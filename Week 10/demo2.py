while True:

    # ...

    answer = 0

    while True:
        try:
            answer = int(input('Do you want to quit [1] or keep going [0]? '))
        except ValueError:
            print('Please enter only 1 (quit) or 0 (keep going)!')
            continue

        if answer == 1:
            break

    # ...
