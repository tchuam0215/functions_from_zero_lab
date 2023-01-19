
import click
from mylib.bot import scrape

@click.command()
@click.option('--name', default="Microsoft", help='Web page we want to scrape')
def cli(name="Microsoft", length=1):
    return click.echo(click.style(f"{scrape(name, length)}", bg="blue", fg="white"))

# print(scrape())
# print(scrape("Facebook"))

# def hello(count, name):
#    for x in range(count):
#        click.echo(f"Hello {name}!")

if __name__ == "__main__":
    cli()