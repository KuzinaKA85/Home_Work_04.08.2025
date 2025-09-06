from src.decorators import log


@log(filename="log.txt")
def my_function(x: int|float, y: int|float) -> int|float:
    return x + y


if __name__ == "__main__":
    my_function(1, 2)
