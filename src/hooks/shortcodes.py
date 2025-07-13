import re
import posixpath
from re import Match

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page

# duplicate of https://github.com/squidfunk/mkdocs-material/blob/master/src/overrides/hooks/shortcodes.py
def on_page_markdown(markdown: str, *, page: Page, config: MkDocsConfig, files: Files):
    # Replace callback
    def replace(match: Match):
        type, args = match.groups()
        args = args.strip()
        
        # Generate project list from files
        if type == "project-list":      return _show_project_list(args, page, files)
        # Tag to indicate a namespace is designed for mapmakers, scripters, or internal
        elif type == "mapping":    return _badge_for_maps(args, page, files)
        # Tag to indicate a namespace is designed for 
        elif type == "scripting":    return _badge_for_scripts(args, page, files)
        # Tag to indicate a class/method should not be used
        elif type == "internal":    return _badge_for_internal(args, page, files)

        # Otherwise, raise an error
        raise RuntimeError(f"Unknown shortcode: {type}")

    # Find and replace all external asset URLs in current page
    return re.sub(
        r"<!-- minrdocs:(\w+)(.*?) -->",
        replace, markdown, flags = re.I | re.M
    )

# -----------------------------------------------------------------------------

# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve_path(path: str, page: Page, files: Files):
    path, anchor, *_ = f"{path}#".split("#")
    path = _resolve(files.get_file_from_path(path), page)
    return "#".join([path, anchor]) if anchor else path

# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve(file: File, page: Page):
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])

# -----------------------------------------------------------------------------

# Create badge
def _badge(icon: str, text: str = "", type: str = ""):
    classes = f"minr-docs-badge minr-docs-badge--{type}" if type else "minr-docs-badge"
    return "".join([
        f"<span class=\"{classes}\">",
        *([f"<span class=\"minr-docs-badge__icon\">{icon}</span>"] if icon else []),
        *([f"<span class=\"minr-docs-badge__text\">{text}</span>"] if text else []),
        f"</span>",
    ])

# Note: change conventions.md to something better
# Create badge for maps
def _badge_for_maps(text: str, page: Page, files: Files):
    icon = "material-tag-outline"
    href = _resolve_path("all_scripts.md#mapping", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Mapping')",
        text = "Mapping",
        type = "map"
    )
    
# Create badge for scripts
def _badge_for_scripts(text: str, page: Page, files: Files):
    icon = "material-tag-outline"
    href = _resolve_path("all_scripts.md#scripting", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Scripting')",
        text = "Scripting",
        type = "script"
    )
    
# Create badge for scripts
def _badge_for_internal(text: str, page: Page, files: Files):
    icon = "material-tag-outline"
    href = _resolve_path("all_scripts.md#internal", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Internal')",
        text = "Internal",
        type = "internal"
    )
    
    
# Create project list
def _show_project_list(text: str, page: Page, files: Files):
    spec = text
    path = f"changelog/index.md#{spec}"

    return "<!-- minrdocs:project-list TODO -->"