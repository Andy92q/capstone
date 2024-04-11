"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ["app.py"]
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={
        "py2app": OPTIONS,
        "py2app": {
            "includes": [ 
                "GUI.py",
                "countDown.py",
                "ExcelFunctions.py",
                "pairing.py",
                "window.py",
            ],
        "resources": ["./databases/*","./classes/*","./excel/*"]
        },
    },
    setup_requires=["py2app"],
)

