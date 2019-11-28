from setuptools import setup

setup(
    name='lilyac',
    version='0.0.22',
    description='',
    author=['Heladio Amaya', 'Cinthya Villegas'],
    author_email=[
        'heladio.ac@gmail.com',
        'cinthyagpe.villegas@gmail.com',
    ],
    packages=['lilyac'],
    install_requires=['PyQt5==5.9.2'],
    entry_points={
        'console_scripts': [
            'lilyac = lilyac.__main__:main'
        ]
    },
)
