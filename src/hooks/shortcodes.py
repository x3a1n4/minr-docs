import glob
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
        if type == "projectlist":      return _show_project_list(args, page, config, files)
        
        # Tag to indicate a utility is designed for mapmakers, scripters, or internal
        elif type == "mapping":    return _badge_for_maps(args, page, files)
        # Tag to indicate a utility is designed for 
        elif type == "scripting":    return _badge_for_scripts(args, page, files)
        # Tag to indicate a class/method should not be used
        elif type == "internal":    return _badge_for_internal(args, page, files)
        
        # Tag to indicate a utility has msc namespaces
        elif type == "msc":    return _badge_for_msc(args, page, files)
        # Tag to indicate a utility has external tools
        elif type == "non_msc":    return _badge_for_non_msc(args, page, files)
        
        # Tag to indicate a utility has a github page
        elif type == "github":    return _badge_for_github(args, page, files)
        # Tag to indicate a utility has a webpage
        elif type == "website":    return _badge_for_website(args, page, files)

        # Tag to indicate is core
        elif type == "core":    return _badge_for_core(args, page, files)

        # Just display text, bypass the badge replacement above
        elif type == "display":     return _display_badge(args, page, files)



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
    icon = "material-pine-tree"
    href = _resolve_path("tags.md#mapping", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Mapping')",
        text = "Mapping",
        type = "map"
    )
    
# Create badge for scripts
def _badge_for_scripts(text: str, page: Page, files: Files):
    icon = "material-code-tags"
    href = _resolve_path("tags.md#scripting", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Scripting')",
        text = "Scripting",
        type = "script"
    )
    
# Create badge for internal
def _badge_for_internal(text: str, page: Page, files: Files):
    icon = "material-tag-outline"
    href = _resolve_path("tags.md#internal", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Internal')",
        text = "Internal",
        type = "internal"
    )
    
# Create badge for msc
def _badge_for_msc(text: str, page: Page, files: Files):
    icon = "material-cube"
    href = _resolve_path("tags.md#msc", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'msc')",
        text = "msc",
        type = "msc"
    )

# Create badge for non-msc tool
def _badge_for_non_msc(text: str, page: Page, files: Files):
    icon = "material-cube-off"
    href = _resolve_path("tags.md#non-msc", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Non-msc')",
        text = "Non-msc",
        type = "non-msc"
    )

# Create badge for github
def _badge_for_github(text: str, page: Page, files: Files):
    icon = "simple-github"
    href = _resolve_path("tags.md#github", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Github')",
        text = f"[Github]({text})",
        type = "github"
    )

# Create badge for website
def _badge_for_website(text: str, page: Page, files: Files):
    icon = "material-web"
    href = _resolve_path("tags.md#website", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Website')",
        text = f"[Website]({text})",
        type = "website"
    )

# Create badge for website
def _badge_for_core(text: str, page: Page, files: Files):
    icon = "octicons-sparkles-fill-24"
    href = _resolve_path("tags.md#core", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Core')",
        text = "Core",
        type = "core"
    )

# display
def _display_badge(text: str, page: Page, files: Files):
    return f"<!-- minrdocs:{text} -->"


# -----------------------------------------------------------------------------
    
# Create project list
def _show_project_list(text: str, page: Page, config: MkDocsConfig, files: Files):
    
    # For each folder in minr_scripts
    # Create the following (example)
    """
    <div class="utility-header" markdown>
    ## **[TeraRabbits](minr_scripts/TeraRabbits/index.md)**
    </div>
    <div class="utility-info" markdown>
    eggshell
    </div>
    <div class="utility-tags" markdown>
    <!-- minrdocs:mapping --> <!-- minrdocs:msc --> <!-- minrdocs:github https://github.com/x3a1n4/minr -->
    </div>
    """
    
    out = ""
    
    # Loop through folders in minr_scripts
    for folder in glob.glob("docs/minr_scripts/*"):
        # Check if folder has an index.md file
        # if so, open it
        with open(folder + "/index.md", "r") as f:
            # It should match the following schema:
            """ 
            <!-- minrdocs:mapping -->
            <!-- minrscript:name Example>
            <!-- minrscript:description This is an example project!>
            """
            # Get the name and description
            firstline = f.readline().strip()
            file = f.read()
            try:
                name = re.search(r"<!-- minrscript:name (.*) -->", file).group(1)
            except AttributeError:
                print(f"Error in {folder}: no name")
                continue
            
            try:
                description = re.search(r"<!-- minrscript:description (.*) -->", file).group(1)
            except AttributeError:
                print(f"Error in {folder}: no description")
                continue
            
            try:
                author = re.search(r"<!-- minrscript:author (.*) -->", file).group(1)
            except AttributeError:
                print(f"Error in {folder}: no author")
                continue
            
            # Create the markdown
            out += f"""
<div class="utility-header" markdown>
## **[{name}]({folder.removeprefix('docs/')}/index.md)**
</div>
<div class="utility-info" markdown>
{author}
</div>
<div class="utility-tags" markdown>
{firstline}
</div>
 - {description}
            """

    out = on_page_markdown(out, page=page, config=config, files=files)
    return out