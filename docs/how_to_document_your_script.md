# How to Document Your Utility

## Why Should I do This?

Do you check all these boxes?

 - [x] I have a script on Minr
 - [x] Other people may find it useful

If so, other people are going to want to use your script! This is the place to tell them how.

!!! note "Why not use the Minr forums?"

    Forums are great for announcements and back-and-forth discussion, but they're _not_ great at hosting documentation. They're much less searchable, much worse at technical formatting (especially code blocks), and account locked. By keeping all the docs in one place, it maximizes the visibility of each project, and thus minimizes the amount of utility scripts players need to re-write for maps.

## How Do I do This?

- Install [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Fork this repo](https://github.com/x3a1n4/minr-docs/fork)
- Add a folder in `./docs/minr_scripts`. Name it something representing your project (usually, the namespace used)
- Add a file `index.md` to your folder. This is the default landing page for your utility!
- Ensure that your `index.md` file starts similar to the following:

<div class="annotate breakword" markdown>
```md
<!-- minrdocs:display mapping --> <!-- minrdocs:display msc --> <!-- minrdocs:display github https://github.com/x3a1n4/minr --> (1)
<!-- utilityinfo:name TeraRabbits --> (2)
<!-- utilityinfo:author eggshells --> (3)
<!-- utilityinfo:dependencies StringHashMap --> (4)
<!-- utilityinfo:description A bundle of Minr scripts to replicate the most useful bits of worldedit + axiom. Often updated. --> (5)
```
</div>
1.  These are the tags shown at the top of the page and on the list in [All Utilities](./all_scripts.md). For the full list of tags, see the [Tags](./tags.md) page or its [source code](https://github.com/x3a1n4/minr-docs/blob/main/docs/tags.md?plain=1)
2.  This is the name of your utility. It will show up as this in the utility list on [All Utilities](./all_scripts.md)
3.  This is you! It can also include anyone who contributed, or anything at all. This shows up as the author on [All Utilities](./all_scripts.md)
4.  This is a comma separated list of all the projects your utility uses as a dependancy. Leave as `<!-- utilityinfo:no_dependencies -->` if your namespace does not use anything else! **This is not currently shown on the docs.** 
5.  This is what your utility does. Try to keep it short if possible, so that it fits on the [All Utilities](./all_scripts.md) list

!!! note "What does this code block mean?"

    This is an example custom header, with something similar specified at the top of all utility `index.md` files. **_You should never need to modify files outside of your utility documentation folder_**. Instead, all the info presented in [All Utilities](./all_scripts.md) is generated on build.

    To learn more, click the :material-arrow-right-circle: symbols in the block above!

- Check that everything looks good by running `mkdocs serve` from the top-level `./minr-docs` folder. Navigate to [localhost:8000](localhost:8000) to view your documentation!

!!! warning "**PermissionError**: [WinError 10013]"

    I ran into this when building this. Poking around, it seemed like there was _already_ something on my 8000 port, and so it was throwing this rather unhelpful error message. Hosting it on a different port with `mkdocs serve -a localhost:XXXX` worked for me.

- [Create a pull request](https://github.com/x3a1n4/minr-docs/pulls)
- DM or ping me on discord `@billy bobby joey` (since that is _unfortunately_ where I'm most active). <sub>If this step gets deleted, it's because I've set up a discord server with a webhook or something. Tell me I need to get on that.</sub> 

??? note "Have tons of documentation?"

    If you have a lot of documentation to add, consider asking me to become a collaborator to the repo! It'll save a bunch of hassle.