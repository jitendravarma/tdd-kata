#add

def check_negative(numbers: list)->list:
    """
    process list for negative numbers
    Input: list[int]
    Oupt: list[int]
    """
    return [num for num in numbers if num < 0]


def handle_delimiter(numbers: str) -> str:
    """
    helper function to handle delimiters eg //;\n
    delimiter will always start with // 
    Input: number: str
    Output: str
    """
    if numbers.startswith("//"):
        # special delimiter will start with // and will be
        # between //and \n, hence we will look for second index
        delimiter = numbers[2:numbers.index('\n')]
        numbers = numbers[numbers.index('\n'):]
        #replace delimiter with comma
        numbers = numbers.replace(delimiter, ",")
    return numbers

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
    
    numbers = handle_delimiter(numbers=numbers)
    #replace emptylines if any
    numbers = numbers.replace("\n", "")
    numbers = list(map(int, numbers.split(',')))
    if negatives := check_negative(numbers=numbers):
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    return sum(numbers)
