#add


def add(numbers:str) -> int:
    """
    function takes a string of numbers and returns 
    their sum. 
    Input: numebers: str
    Returns: int
    """
    # return 0 for empty string
    if not numbers:
        return 0
    if numbers.startswith("//"):
        # special delimiter will start with // and will be
        # between //and \n, hence we will look for second index
        delimiter = numbers[2:numbers.index('\n')]
        numbers = numbers[numbers.index('\n'):]
        #replace delimiter with comma
        numbers = numbers.replace(delimiter, ",")
    #replace emptylines if any
    numbers = numbers.replace("\n", "")
    numbers = list(map(int, numbers.split(',')))
    return sum(numbers)
