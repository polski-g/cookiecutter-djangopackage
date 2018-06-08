{{cookiecutter.project_name}}
===

{{cookiecutter.project_short_description}}


Quickstart
===

Install {{cookiecutter.project_name}}:

    pip install -e git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
    
Add it to your `INSTALLED_APPS`:
    
    INSTALLED_APPS = (
        ...
        '{{cookiecutter.app_name}}',
        ...
    )
    
