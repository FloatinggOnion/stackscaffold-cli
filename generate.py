from cookiecutter.main import cookiecutter
import os

# use cookiecutter to generate it
# start with cookiecutter-react-django and then build your own cookiecutter templates
# def init_project(project_name, backend_framework, frontend_framework):

#     # create a new project directory; raise an error if it already exists
#     project_dir = os.path.join(os.getcwd(), project_name)
#     os.makedirs(project_dir, exist_ok=False)

    
def generate(project_name, project_slug):
    # create a new project directory; raise an error if it already exists
    project_dir = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_dir, exist_ok=True)

    # generate the project
    # add progress bar while generating the project

    cookiecutter('https://github.com/ohduran/cookiecutter-react-django', output_dir=project_dir, no_input=True, extra_context={'project_name': project_name, 'project_slug': project_slug})