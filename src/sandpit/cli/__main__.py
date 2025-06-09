from sandpit import __app_name__
from sandpit.cli import cli


def main():
    cli.app(prog=__app_name__)


if __name__ == "__main__":
    main()
