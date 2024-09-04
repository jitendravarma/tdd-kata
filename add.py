#add


def add(numbers:str) -> int:
    """
    function takes a string of numbers and returns 
    their sum. 
    Input: numebers: str
    Returns: int
    """
    numbers = numbers.replace("\n", "")
    if not numbers:
        return 0
    numbers = list(map(int, numbers.split(',')))
    return sum(numbers)
