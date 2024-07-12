import typer
from typing import Optional
from rich import print
from rich.progress import track, Progress
from rich.panel import Panel
from rich.prompt import Prompt

import time

from generate import generate

app = typer.Typer()


@app.command()
def init(name: Optional[str] = ''):
    '''
    Initialise a project.
    '''
    print(Panel.fit("[bold green]Welcome, to StackScaffold!:rocket:"))

    # total = 0
    # for value in track(range(100), description="Processing..."):
    #     # Fake processing time
    #     time.sleep(0.1)
    #     total += 1

    if not name: 
        # project_name = input('What is your project name?(default is "my-project"): ')
        project_name = Prompt.ask('What is your project name?', default='my_project')
        project_slug = Prompt.ask('Project Slug (the name of your project repo): ', default=project_name)
    frontend = input('What do you choose for frontend?\n [1] React \n More will be added later...sorry \n Answer here: ')
    backend = input('What do you choose for backend?\n [1] Django \n [2] FastAPI \n More will be added later...sorry \n Answer here: ')
    
    # Starting the project
    print(f"Nice name! Let's start [green]{project_name}[/green]")

    # create a progress bar that lasts the time of the project generation
    with Progress() as progress:
        task = progress.add_task("[green]Generating project...", total=100)
        generate(project_name, project_slug, frontend, backend, progress, task)
    
    


if __name__ == "__main__":
    app()