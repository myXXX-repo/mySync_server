# mySync server

### environment requirement

    >= python3.5

    - flask
    - os
    - json
    - time
    - argparse
    - flask-sqlalchemy
    - flask-script

    tip for development:

    use windows subsystem linux with python-venv

    For my personality, I don't like to code upon pure Windows environment, wsl could be one good choice.

### directory tree

    +--mySync/
    |   +--apps/ (locate apps)
    |   |   +--Git
    |   |   +--Markdown
    |   |   +--Sticky
    |   |   +--Main
    |   +--common/ (common libs)
    |   |   +--__init__.py
    |   |   +--libs.py
    |   |   +--ext.py
    |   +--config/ (server config)
    |   |   +--__init__.py
    |   |   +--errorpage.py
    |   +--templates/ (view page templates)
    |   |   +--template.html
    |   |   +--temp.html
    |   |   +--index.html
    |   +--static/ (static files for templates)
    |   |   +--...
    +--data/ (store data, auto create)
    |   +--markdown/
    +--manage.py

### server usage

    python3 manage.py runserver
    usage: 
        [-?] [-h HOST] [-p PORT] [--threaded]
        [--processes PROCESSES] [--passthrough-errors] [-d]
        [-D] [-r] [-R] [--ssl-crt SSL_CRT]
        [--ssl-key SSL_KEY]
    default:
        host http://127.0.0.1
        port 5000
        debug mode off
        
             

### api usage

#### *Sticky*

    http://host:port/v2.1/Sticky

        all ids are added while program running, there are no id param in json

    - GET: get all Sticky by one json array str

        support Sticky number limit, by adding param limit=<int:limit>
        TODO: is going to support more limit

    - POST: add new Sticky

    

    http://host:port/v2.1/Sticky/<int:resid_raw>

    - GET: get certian Sticky

    - PUT: upload certian Sticky to cover list item

    - PATH: take path on data of item in list

    - DELETE: DELETE all Sticky
    
#### *Markdown*
#### *Statistics*
#### *Git*
#### *Config*
#### **

    
