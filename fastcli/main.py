from distutils.dir_util import copy_tree
import emoji
import traceback
import click
import os


def take_path_of_file(path):
    return '/'.join(path.split('/')[:-1])


@click.group()
def cli():
    pass


@click.command()
@click.argument('name')
def create(name):
    try:
        click.clear()

        start = f"{take_path_of_file(__file__)}/src"
        end = f"{os.getcwd()}/{name}"

        click.echo("\nMaking the project\n")

        copy_tree(start, end)

        os.chdir(end)
        click.echo("Starting git repository\n")
        os.system("git init")

        click.echo(emoji.emojize("\n\nDone! :rocket: \n\n",variant="emoji_type"))
    except Exception as error:
        print(f"Error:\n{error}\n\n")
        traceback.print_exception()


cli.add_command(create)


if __name__ == '__main__':
    cli()
