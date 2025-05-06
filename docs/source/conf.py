# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Colosseum'
copyright = '2025, Colosseum @ Northeastern University WIoT'
author = 'Colosseum'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Logo

html_logo = "_static/resources/index/logo.png"

html_theme_options = {
    "logo_only": False,
    "display_version": True
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
