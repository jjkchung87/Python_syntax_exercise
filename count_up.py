def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    # arr = list(range(start,stop+1))
    # for num in arr:
    #     print(num)

    #solution

    while start <= stop:
        print(start)
        start = start + 1


count_up(5, 7)        
