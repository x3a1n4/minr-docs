![Image title](images/thisisaheaderimage.png){ align=left }

# Minr Player Utility Documentation

This is a [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) website for hosting documentation for the tools written by players for the server [`zero.minr.org`](https://zero.minr.org). Conceptually similar to the [celeste helper list](https://maddie480.ovh/celeste/custom-entity-catalog).

!!! note "What is this site for?"

    This site is for all minr players! 

    - It's for mappers, who want to find mapping-oriented tools, such as [TODO: example] or [TODO: example]. Any utility tagged with <!-- minrdocs:mapping --> can be imported and used, with no scripting neccessary.
    - It's for scripters, who want to know what to build off of. Ever wanted to [TODO: example]? Any utility tagged with <!-- minrdocs:scripting --> is a library that you can use in your code.
    - It's for players, who get better maps!

### Check out all documented utilities at **[All Utilities](./all_scripts.md)** 

### For information on how you can document your scripts here, check out **[How to Document Your Utility](./how_to_document_your_script.md)**

??? warning "A Note About Dependencies"

    In the javascript world, there's an environment known as Node.js. You've encountered it if you've ever tried to write a discord bot. It's the most popular backend environment that exists. 

    And with that popularity comes hell. Specifically, dependancy hell. Node.js is _infamous_ for its sprawling dependancy trees, leading to nigh-undebuggable problems. You can install the package [`everything`](https://everything.npm.lol), which has over a million dependancies and will instantly ban you from npm. The package [`is-even`](https://www.npmjs.com/package/is-even) checks if a number is even, and had 165,708 downloads this week.

    Minr is _probably_ worse.

    If you use a namespace that you don't control, and _especially_ if you use a namespace that you don't have the source code of, it's succeptible to _all sorts_ of problems.

    - Data loss from the code updating
    - Data loss from somebody else using the namespace the wrong way
    - Unexpected functionality changing when code updates
    - The utility doesn't work as it should
    - The utility has an exploit, causing all dependants to be succeptible
    - *And so on...*

    For these reasons, the <!-- minrdocs:core --> tag exists. These are utilities that are widely-used, safe to use, or otherwise reputable in the community. If you're looking for specific functionality, seek these out first, and use your best judgement before building on top of newer, smaller utilities.
    
    Ultimately, I can't really speak more about this, since I have no software infrastructural skills. So I'll stop here. Hopefully together, we can avoid a minr [left-pad incident](https://en.wikipedia.org/wiki/Npm_left-pad_incident) (you guessed it, also Node.js! Incredible piece of software that is)