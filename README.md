ale-cli/
```│
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── model.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_model.py
│
├── pyproject.toml
├── README.md
└── requirements.txt
```


## Install command

0) Make sure the .py file you want to use as command has as first line:

`#!/usr/bin/env python or #!/usr/bin/env python3`

1) If does not exist, create a local bin folder (under the user /):

`$ mkdir -p ~/bin`

2) Copy the file cli.py file without the .py extension:

$ cp cli ~/bin/<command_name>

3) Make the file executable

`$ sudo chmod +x ~/bin/<command_name>`

4) Finally export bin path

`export PATH=$PATH":$HOME/bin"  OR cp cli ~/.local/bin/<command_name>`
