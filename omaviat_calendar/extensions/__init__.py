import importlib
import os

__version__ = "0.1.0"

files_extensions = os.listdir("omaviat_calendar/extensions")
for file in files_extensions:
    if file.startswith("extensions"):
        importlib.import_module(f"omaviat_calendar.extensions.{file[:-3]}")
