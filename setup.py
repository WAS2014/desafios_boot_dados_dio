from setuptools import setup, find_packages

with open ("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitines()

setup(
    name="terceiro_desafio",
    version= "0.0.1",
    author= "warley_a_souza",
    author_email= "warley.de@gmail.com",
    description= " Meu terceiro desafio",
    long_description=page_description,
    long_description_content_type="text/markdow",
    url=https://github.com/WAS2014/desafios_boot_dados_dio
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',   
)    

