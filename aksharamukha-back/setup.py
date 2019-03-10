import sys
from cx_Freeze import setup, Executable

import pkgutil
from importlib import import_module
import ScriptMap

dynamicImports = []

for importer, modname, ispkg in pkgutil.iter_modules(ScriptMap.__path__):
  for importer, submodname, ispkg in pkgutil.iter_modules(import_module('ScriptMap.'+modname).__path__):
    dynamicImports.append('ScriptMap.' + modname + '.' +  submodname)

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["asyncio", "idna", "jinja2"] + dynamicImports}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])