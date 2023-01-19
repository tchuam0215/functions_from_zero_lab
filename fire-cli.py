import fire
from mylib.bot import scrape

def fire_cli(name, length=1):
    #return 'Hello {name}!'.format(name=name)
    """
        Fire is one of the easiest cli tools in python.
        here is one example.
    """
    return scrape(name, length)

if __name__ == '__main__':
    fire.Fire(fire_cli)