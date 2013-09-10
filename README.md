The Great Atlas Templates
=========================

What It's About
---------------

[Surrender@20](http://www.surrenderat20.net/)'s [Great Atlas](http://www.surrenderat20.net/p/great-atlas.html) features a few handy cards giving quick information about champions in League of Legends. I thought it was a waste having all this information in images and using Photoshop to manually create these cards, so I just went for it.

After some hours of testing the hosters of S@20 decided they would stick with jpg images which made my efforts pretty much in vain, but I learnt something which will be presented in the following section(s). If *you* would like to continue working on this, **please do**! That's the reason I actually put it on github in the first place. It's just that I don't consider this to be worth my time anymore since I have other priorities now.

I worked on the [Ryze card](http://3.bp.blogspot.com/-8tgmGAJcwWI/UUn_lsvFB-I/AAAAAAAABIQ/voiVakJvGDI/s2200/Ryze.jpg).

A preview of the pre-compiled WIP state of Ryze's card can be found in `ryze.html` and viewed [here](https://raw.github.com/FichteFoll/atlas-templates/master/ryze.html).


Background
----------

I had the idea for quite a while before I eventually proposed it to the [feedback post](http://www.surrenderat20.net/2013/08/the-great-atlas-feedback-mini-contest.html#comment-1007284907), after which I was asked to prepare something like this.

### The Plan

Well, the plan was pretty simple: Use a bunch of abstaction languages to circumvent XML and ease editing by hand to construct very similar looking pages with just a few content differences. If you looked at the cards I linked at the top you know what I mean.

Then I tried to replicate the card design in a HTML structure and styling it with some CSS3. CSS2 was not an option since it would complicate all the rounded borders, box/text shadows and color gradients to an unaffordable amount.

### Process

#### Abstraction Languages

YAML has been a very joyous discovery since it's SO AWESOME. Really. I've also worked with YAML a few times already and know its syntax and how to use it (in Python).

I hate XML (and thus HTML) wholeheartedly, so I searched for a HTML abstraction language that was capable of running simple templates and is standalone, since I want to generate the HTML at command and not automatically using a framework (e.g. Django, Jinja2 or Rails).

The first thing coming to mind was HAML, probably the first abstraction actually, but it relies on Rails and uses Ruby expressions for its templates. I don't know any Ruby at all, so I avoided it. I then found [HamlPy](https://github.com/jessemiller/HamlPy/) which is basically Haml for Django, but again it had an external dependency which I didn't like so I continued searching. I eventually found [dmsl](https://github.com/dskinner/dmsl), which features almost complete Python expression support and I really liked the syntax. This was exactly what I imagined. The author [discouraged](https://github.com/dskinner/dmsl/issues/27) me from using it since it had many bugs and I should rather use his new Go project called [damsel](https://github.com/dskinner/damsel). However, know even less about Go than about Ruby and I didn't even get how I was supposed to use it (with templates at least), so that was not really promising and I just chose the Python dmsl.

Now that the HTML abstraction had been settled I had to search for a CSS abstaction, since I also didn't like that too much. Apparently, I already knew [SASS/SCSS](http://sass-lang.com/) and it's also standalone, so I didn't have to do much (except install Ruby).

#### Working on the template

I had the layout in mind already so I began outlining the structure in many &lt;div&gt;s. After that I tried to structure these with positional definitions in CSS. I had a really hard time with the table-like layout of the first header (text on the left, image on the right) and all my `float: right` attempts didn't look to well. Once I finished that I encountered the real problem: vertically centering content.

You won't believe [how hard](http://blog.themeforest.net/tutorials/vertical-centering-with-css/) it is to vertically center some content in such a common setup (HTML and CSS). Literally every option had a downside, even after decades of the internet. I eventually chose to use `display: table-cell` and `vertical-align: middle`, ditching IE8 support since it didn't handle that, but it was one of the lesser evils and pretty simple to use. I then decided to use the pseudo-table layout everywhere on the page since it would break anyway if I used it once, which made things a bit easier from then onwards.

I tried to extract the background pattern from the `psd` file I got (for templating purposes) and I failed horribly since Photoshop uses some exotic format for its patterns (why?). So instead I cut it off the image itself, made sure I cut it at the correct positions to get a seamless transition for the repetitions. It turned out pretty well, except that it was limited to the one color (and size) I cut it out with. I decided to use Gimp and turn the background color "to transparency" and used the previous color as CSS background-color instead. This allowed me to reuse the pattern for the boxes (where it actually has a smaller scale but I didn't extract that yet) without it becoming almost invisible due to too many color overlays.

After that I didn't really encounter any major problems, considering the following was mainly text and I actually stopped working on this shortly afterwards.


### WIP state

This is supposed to be a small list/draft of what I still have in mind, if anyone cares to continue on this (including myself), without too much detail:

- Finish the template
- Extract images from the card
- Add icons for items, skills and champions
- Add references for all these in the respective `.yaml` file
- Copy data from the card(s)
- Write functions that process the texts and highlight abilities, damage type and champion class as dynamically as possible
- Add the fonts
- Create alternative template for champions with two abilities (Lee Sin, Jayce)


### The YAML File

In the end, the YAML file should contain information about:

- Champion name
- Champion title
- Champion image location
- Description
- Damage details
- Slider positions
- Utility and Mobility info
- Items
    - Name (image path should be determined by that)
    - Type (Offensive, Defensive, Utility)
    - Description
- Counters
    - Champions
        - Name (icon)
        - Text
    - Overview Text
    - Items
        - Name (icon)
        - Text
- Abilities
    - Name (icon)
    - Spell (Passive, Q, W, R)
    - Text
- Tips
    - Author
    - Phrase
    - Text
- Tags


Contributing
------------

Fork it, work on it, throw it away, forget about it; do whatever you want. I'd love to see pull requests that improve the template itself or add some data for the other champions. If you are keen on maintaining this I'd also love to make you contributer by giving repo access.