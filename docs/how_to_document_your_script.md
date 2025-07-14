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
- Fork [this repo](https://github.com/x3a1n4/minr-docs)
- Add a folder in `./docs/minr_scripts`
- Add file `index.md` to your folder. This is the default landing page for your utility.
- Ensure that your `index.md` file starts similar to the following:

<div class="annotate breakword" markdown>
```md
<!-- minrdocs:display scripting --> <!-- minrdocs:display msc --> <!-- minrdocs:display github https://github.com/x3a1n4/minr --> (1)
<!-- minrscript:name StringHashMap --> (2)
<!-- minrscript:author eggshells --> (3)
<!-- minrscript:description A small implementation of string:string hashmaps in minr --> (4)
```
</div>
1.  These are the tags shown at the top of the page and on the list in [All Utilities](./all_scripts.md). For the full list of tags, see the [Tags](./tags.md) page or its [source code](https://github.com/x3a1n4/minr-docs/blob/main/docs/tags.md?plain=1)
2.  This is the name of your utility. It will show up as this in the utility list on [All Utilities](./all_scripts.md)
3.  This is you! It can also include anyone who contributed, or anything at all. This shows up as the author on [All Utilities](./all_scripts.md)
4.  This is what your utility does. Try to keep it short if possible, so that it fits on the [All Utilities](./all_scripts.md) list

- Check that everything looks good by running `mkdocs serve` and navigating to [localhost:8000](localhost:8000)

!!! note "**PermissionError**: [WinError 10013]"

    I ran into this when building this. Poking around, it seemed like there was _already_ something on my 8000 port, and so it was throwing this rather unhelpful error message. Hosting it on a different port with `mkdocs serve -a localhost:XXXX` worked for me.

- Create a pull request 
- DM or ping me on discord `@billy bobby joey` since that is _unfortunately_ where I'm most active. If this step gets deleted, it's because I've set up a discord server with a webhook to ping me every time a PR gets made. 

!!! note "Advanced: Using Submodules"

    If you want to host the documentation on your own repository, you can achieve this with a _subrepository_. I'm not entirely sure how to do this, but check out [this submodules explanation](https://gist.github.com/gitaarik/8735255) and [this folder explanation](https://gist.github.com/ZhuoyunZhong/2c08c8549616e03b7f508fea64130558) for more info. I'll try to throw up a proper explanation later.