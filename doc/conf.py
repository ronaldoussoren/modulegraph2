import os
import sys


def get_version():
    fn = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "modulegraph2",
        "__init__.py",
    )
    for ln in open(fn):
        if ln.startswith("__version__"):
            version = ln.split("=")[-1].strip().strip('"')
            return version


# Add root of the tree to sys.path for autodoc
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path[0])


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named "sphinx.ext.*") or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx_sitemap",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    "sphinxcontrib.mermaid",
    "sphinx_reredirects",
    "sphinxext.opengraph",
    "sphinxcontrib.jquery",
    "sphinx_datatables",
]

extlinks = {
    "issue": ("https://github.com/ronaldoussoren/pyobjc/issues/%s", "#%s"),
    "pr": ("https://github.com/ronaldoussoren/pyobjc/pull/%s", "#%s"),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "modulegraph2"
copyright = "2010-2025, Ronald Oussoren"

# The short X.Y version.
version = get_version()

# The full version, including alpha/beta/rc tags.
release = version

# List of directories, relative to source directory, that shouldn"t be searched
# for source files.
exclude_patterns = ["_build", "tmp"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently "default" and "sphinxdoc".
# html_theme = "default"
html_theme = "shibuya"

html_theme_options = {
    "accent_color": "jade",
    "color_mode": "auto",
    "nav_links": [
        {
            "title": "GitHub",
            "url": "https://github.com/ronaldoussoren/modulegraph2",
            "external": True,
        },
        {
            "title": "Support Me",
            "url": "https://blog.ronaldoussoren.net/support/",
            "external": True,
        },
        {
            "title": "Resources",
            "children": [
                {
                    "title": "Changelog",
                    "url": "changelog",
                    "summary": "Overview of updates",
                },
            ],
        },
    ],
    "globaltoc_expand_depth": 1,
    "github_url": "https://github.com/ronaldoussoren/pyobjc",
    "mastodon_url": "https://blog.ronaldoussoren.com/@ronald",
}

html_baseurl = "https://modulegraph2.readthedocs.io/"

html_extra_path = ["_extra"]

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {"**": ["localtoc.html", "links.html", "donate.html", "searchbox.html"]}

# Output file base name for HTML help builder.
htmlhelp_basename = "modulegraph2doc"


# -- Options for LaTeX output --------------------------------------------------

# The paper size ("letter" or "a4").
latex_paper_size = "a4"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "modulegraph2.tex",
        "modulegraph2 Documentation",
        "Ronald Oussoren",
        "manual",
    )
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "objectgraph": ("https://objectgraph.readthedocs.io/", None),
}

todo_include_todos = False
blockdiag_html_image_format = "svg"
blockdiag_debug = True
