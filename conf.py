# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Sling TV on Samsung Smart TV'
copyright = '2025, Sling'
author = 'Sling TV Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Use Sling TV on Samsung Smart TVs – Update & Activation Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Sling TV Samsung Setup"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Theme options
# html_theme = 'sphinx_rtd_theme'  # Uncomment if you use the Read the Docs theme

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have images, JS, or CSS

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
