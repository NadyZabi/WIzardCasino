""" fatory method for all useful stuff creation """
from flask import Flask




# MVC structure:
"""
app.py - contains falsk instance but not the app creation code

controller.py - everythoing in between: which url was called, what parameters there are, what should i do with the data (preparation, filter, aggregation, etc.) and prepare it for further call from view

view.py - contains function with "render_template"

models.py - contains you DB models or DataFrame and maybe schema for csv

"""
