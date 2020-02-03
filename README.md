# mySync server

### environment requirement

    python3

    - flask
    - os
    - json
    - time
    - argparse

    tip for development:

    use windows subsystem linux with python-venv

    For my personality, I don't like to code upon pure Windows environment, wsl could be one good choice.

### directory tree

    +--static/
    |   +--favicon.ico
    |   +--index.js
    |   +--index_sticky.js
    +--templates/
    |   +--template.html
    |   +--temp.html
    |   +--index.html
    +--data/ (auto create)
    |   +--markdown/
    |   +--sticky.json
    +--app.py

### server usage

    python3 app.py
      --listen -l <str:listen> default: 0.0.0.0
      --port -p <int:port> default: 5000
      --debugOn -d <bool:debugOn> default: False

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

    

