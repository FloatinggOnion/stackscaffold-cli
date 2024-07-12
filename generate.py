from cookiecutter.main import cookiecutter
import os
from rich.prompt import Prompt
from rich.progress import Progress

# use cookiecutter to generate it
# start with cookiecutter-react-django and then build your own cookiecutter templates
# def init_project(project_name, backend_framework, frontend_framework):

#     # create a new project directory; raise an error if it already exists
#     project_dir = os.path.join(os.getcwd(), project_name)
#     os.makedirs(project_dir, exist_ok=False)

    
def generate(project_name, project_slug, frontend, backend, progress: Progress, task):
    # create a new project directory; raise an error if it already exists
    project_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir, exist_ok=True)

    # generate the project
    # add progress bar while generating the project
    
    # simulate project steps
    steps = 4

    def update_progress(step):
        progress.update(task, advance=100/steps)

    # step 1: Initial setup
    print('Setting up project directory...')
    update_progress(1)

    # setp 2: Generate the project
    if frontend == '1' and backend == '1':
        print('Generating project with React and Django...')
        cookiecutter('https://github.com/ohduran/cookiecutter-react-django', output_dir=project_dir, no_input=True, extra_context={'project_name': project_name, 'project_slug': project_slug})

    elif frontend == '1' and backend == '2':
        port = Prompt.ask('What is your project port number? ', default='8000')
        postgres_user = Prompt.ask('PostgreSQL user: ', default='postgres')
        postgres_password = Prompt.ask('PostgreSQL password: ', default='postgres')
        postgres_db = Prompt.ask('PostgreSQL database name: ', default='postgres')
        superuser_email = Prompt.ask('Superuser email: ', default='test@test.com')
        superuser_password = Prompt.ask('Superuser password: ', default='test1234')
        secret_key = Prompt.ask('Secret key: ', default='secret')

        print('Generating project with React and FastAPI...')
        cookiecutter('https://github.com/Buuntu/fastapi-react', output_dir=project_dir, no_input=True, extra_context={'project_name': project_name, 'project_slug': project_slug, 'port': port, 'postgres_user': postgres_user, 'postgres_password': postgres_password, 'postgres_database': postgres_db, 'superuser_email': superuser_email, 'superuser_password': superuser_password, 'secret_key': secret_key})

    # step 3: Finalizing
    print('Finalizing...')
    update_progress(1)

    # step 4: Done
    print('Project generation complete!')
    update_progress(1)