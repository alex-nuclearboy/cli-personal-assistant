from setuptools import setup, find_namespace_packages

setup(
    name='Personal Assistant',
    version='1.1',
    description='Data and File Assistant',
    author='Hufflepuff',
    author_email='alex.nuclearboy@gmail.com',
    license='GPL-3.0 license',
    packages=find_namespace_packages(),
    install_requires=['prompt_toolkit', 'pygments', 'tabulate', 'termcolor'],
    long_description='The "Personal Assistant" bot is designed to assist users\
          in managing their contacts, notes, and files through a natural\
          language interface. The bot leverages advanced functionalities\
          to understand user input and provide relevant suggestions\
          based on context.',
    url='https://github.com/alex-nuclearboy/cli-personal-assistant.git',
    entry_points={
        'console_scripts': [
            'personal-assistant = src.main:main'
        ],
    },
)
