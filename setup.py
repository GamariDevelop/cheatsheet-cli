from setuptools import setup, find_packages


setup(
    name="cheatsheet",
    version="0.0.2",
    description="CLIでCheatsheetの管理を行うツール。",
    author="gamari",
    packages=find_packages(),
    install_requires=['fire', 'inquirer'],
    entry_points={
        'console_scripts': [
                'cheat=src.app_cheat:main',
        ],
    }
)
