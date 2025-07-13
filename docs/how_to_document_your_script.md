# How to Document Your Script

## Why Should I do This?

Do you check all these boxes?

 - [x] I have a script on Minr
 - [x] Other people may find it useful

If so, other people are going to want to use your script! This is the place to tell them how.

??? note "Why not use the Minr forums?"

    Forums are great for announcements and back-and-forth discussion, but they're _not_ great at hosting documentation. They're much less searchable, much worse at technical formatting (especially code blocks), and account locked. By keeping all the docs in one place, it maximizes the visibility of each project, and thus minimizes the amount of utility scripts players need to re-write for maps.

## How Do I do This?

- Install [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- Fork [this repo](https://github.com/x3a1n4/minr-docs)
- Add a subrepository in `./docs`
- Check that everything looks good by running `mkdocs serve` and navigating to [localhost:8000](localhost:8000)

??? note "**PermissionError**: [WinError 10013]"

    I ran into this when building this. Poking around, it seemed like there was _already_ something on my 8000 port, and so it was throwing this rather unhelpful error message. Hosting it on a different port with `mkdocs serve -a localhost:XXXX` worked for me.

- Create a pull request