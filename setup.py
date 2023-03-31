from setuptools import setup, find_packages

setup(
    name='Jeu de lettre',
    version='1.0.0',
    author='Vituixo',
    author_email='victoirenoyouliwa@gmail.com',
    packages=find_packages(),

    include_package_data=True,
    install_requires=[
        'tkinter',
        'random',
        'json'
    ],
    entry_points={
        'console_scripts': [
            'app=app.__main__:main'
        ],
    }
)
