import cloup


@cloup.group()
def main():
    """Main CLI application"""
    pass


@main.group()
def operations():
    """Maths operations"""
    pass


@operations.command()
@cloup.argument('x', type=int, help="First Argument")
@cloup.argument('y', type=int, help="Second Argument")
def add(x: int, y: int) -> int:
    """Add two numbers"""
    return x + y


@operations.command()
@cloup.argument('x', type=int, help="First Argument")
@cloup.argument('y', type=int, help="Second Argument")
def subtract(x: int, y: int) -> int:
    """Subtract two numbers"""
    return x - y


@operations.group(name = 'advanced')
def advanced_operations():
    """Advanced operations"""
    pass


@advanced_operations.command()
@cloup.argument('x', type=int, help="First Argument")
def square(x: int) -> int:
    """Square a number"""
    return x * x


@main.group()
def other_operations():
    """Other operations"""
    pass


@other_operations.command(name = 'add')
@cloup.argument('x', type=float, help="First Argument")
@cloup.argument('y', type=float, help="Second Argument")
def addf(x: float, y: float) -> float:
    """Add two float numbers"""
    return x + y


@other_operations.command(name = 'subtract')
@cloup.argument('x', type=float, help="First Argument")
@cloup.argument('y', type=float, help="Second Argument")
def subtractf(x: float, y: float) -> float:
    """Subtract two float numbers"""
    return x - y


if __name__ == "__main__":
    main()