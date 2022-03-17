# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CHMap'
copyright = '2019, The Max Planck Institute for the History of Science, The Department of History of Shanghai Jiao Tong University. Land Survey Maps of China: A Cartographic Database (MPIWG Dataset: 1885-1945, 1:50,000), The General Administration of Land Surveys. https://chmap.mpiwg-berlin.mpg.de. Published 2019. '
author = 'Spencer Forbes'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
