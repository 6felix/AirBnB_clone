#!/usr/bin/python3
"""Initialization of the model package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
