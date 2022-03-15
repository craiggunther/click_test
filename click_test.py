import click

"""This is introductory docstring #1 at the top of the file."""

def someFunction():
    """Here is docstring #2 for a function named someFunction()."""

class someClass:
    def someMethod():
        """Here is docstring #3 for the someMethod() in the someClass."""

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', default="Craig", help='The person to greet.')
def hello(count, name):
    """Here is docstring #4 for the 'click' decorated hello() function.
    Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
