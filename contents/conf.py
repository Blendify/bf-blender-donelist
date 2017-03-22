
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join('..', 'exts')))

extensions = ['bl_commit', 'bl_diff', 'bl_task']

# The suffix of source filenames.
source_suffix = '.rst'

exclude_patterns = ["template.rst"]
master_doc = 'index'

# General information about the project.
project = 'Weekly Done-List of Blendify'
copyright = 'Creative Commons'

# without this it calls it 'documentation', which it's not
html_title = "weekly-donelist-blendify"
html_short_title = "blendify's weekly done-list"

# visual noise for my purpose
html_show_copyright = False
html_show_sphinx = False
html_show_sourcelink = False

'''
try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if sphinx_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
else:
    html_theme = 'haiku'

if sphinx_rtd_theme:
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
'''

html_theme = 'alabaster'
html_theme_options = {
    "show_powered_by": False,
    }
import alabaster
print(alabaster.__file__)
html_theme_path = [alabaster.get_path()]


# for our own extensions!
phabricator_base = "http://developer.blender.org"

