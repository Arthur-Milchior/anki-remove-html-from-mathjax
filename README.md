# Remove html from mathjax
## Rationale
If by accident you did add some formatting to some text you intended
to use with mathjax, the mathjax won't display. You'll simply have
some text insde a pair `\(\)` or `\[\]`. This add-on simply clean all
the notes by removing the formatting in mathjax and allowing it to be formatted.

It also prints in the terminal all change done.

## Warning
This may affect potentially your whole collection; so there is a small
risk that it does change you don't expect; especially if you use `\(`,
`\)`, `\[`, `\]` outside of mathjax, or if anki didn't detect that
some `<` was not some html and didn't replace it with `&lt;`
## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU GPL, version 3 or later; http://www.gnu.org/licenses/gpl.html
Source in   | https://github.com/Arthur-Milchior/anki-remove-html-from-mathjax
Addon number| [???????](https://ankiweb.net/shared/info/???????)
