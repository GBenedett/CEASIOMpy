#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------
import os
import sys

from ceasiompy.__version__ import __version__

NAME = 'CEASIOMpy'

sys.path.insert(0, os.path.abspath('../../lib/'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------
project = NAME
copyright = '2019, CFS Engineering'
author = 'CFS Engineering'

# version: The short X.Y version
# release: The full version, including alpha/beta/rc tags
# version = ''
version = __version__

# ===============
# AUTOMATE THINGS
# ===============

# Update the auto-docs
os.system('bash ./dev_doc/gen_auto_doc.sh')

# Update the module-dependecy pages
os.system('python3 user_guide/gen_module_interface_pages.py')

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    # 'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]

# Paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Source file parsers
# source_parsers = {
#         '.md': 'recommonmark.parser.CommonMarkParser',
#         }

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

rst_prolog = f"""
.. |name| replace:: {NAME}
.. |name_bold| replace:: **{NAME}**
.. |author1| replace:: {author}
.. |license| replace:: *Apache-2.0*
.. _Github: https://github.com/cfsengineering/CEASIOMpy
.. _pip: https://pypi.org/project/pip/
"""

# -- Options for HTML output -------------------------------------------------

# html_theme = 'classic'
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'canonical_url': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

# Paths that contain custom static files (such as style sheets) relative to this directory.
html_static_path = ['_static']

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = f'{NAME}doc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': '',

    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'{NAME}.tex', f'{NAME} Documentation', f'{author}', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, f'{NAME}', f'{NAME} Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, f'{NAME}', f'{NAME} Documentation',
     author, f'{NAME}', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------
