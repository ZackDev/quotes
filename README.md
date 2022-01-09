# quotes

A *python3* program to display quotes from whom or whatever you like.

## How to run it:

Type `python3 main.py` into a terminal to display the quotes contained in the `cites.xml` file.

## What the `cites.xml` should contain:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stoic>
  <author name="Marcus Aurelius" image="marcus_aurelius.png">
    <cite>You have power over your mind - not outside events. Realize this, and you will find strength.</cite>
  </author>
  <author>
    <cite>If the will is strong there is no mountain too hard to climb.</cite>
    <cite>...</cite>
  <author>
</stoic>
```

* the root tag `<stoic>...</stoic>` is exchangeable.
* `<cite></cite>` needs to be encapsulated by the `<author></author>` tag
* providing a `name` and `image` attribute is optional
  * providing no `name` attribute defaults to the name set to *Unknown*
  * not providing an `image` attribute displays the *default.png*
* the image's default path is `./img/`, add them there

## Used custom Fonts in PostcardView:
[Line 18](https://github.com/ZackDev/quotes/blob/main/view.py#L18) - [1942 Report](https://www.dafont.com/1942-report.font)

[Line 23](https://github.com/ZackDev/quotes/blob/main/view.py#L23) - [Photograph Signature](https://www.dafont.com/photograph-signature.font)

![Ancient Ruins](./img/default.png)
