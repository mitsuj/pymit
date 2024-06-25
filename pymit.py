#!/usr/bin/env python3

import os

name = input("Enter the name for your new directory: ")
print(f"Creating directory at: {os.path.expanduser(f'~/Projects/{name}')}")
os.mkdir(os.path.expanduser(f"~/Projects/{name}"))

os.system(f"cd ~/Projects/{name} && poetry init -n")
os.system(f"cd ~/Projects/{name} && poetry add black isort pylint mypy --group dev")
os.system(f"cd ~/Projects/{name} && touch README.md")
os.system(f"cd ~/Projects/{name} && cp ~/LICENSE.txt ./LICENSE")
os.system(f"cd ~/Projects/{name} && git init")


os.system(
    f"cd ~/Projects/{name} && curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
)


os.system(f"code ~/Projects/{name}")

print("Done!")
