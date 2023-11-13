# Retailwind

Reverse obfuscated tailwind classes

![app](/assets/retailwind.gif)

## Install

```shell
pip install retailwind
```

## Usage

You can either use it as a CLI tool, an interactive terminal app or a python library. In all cases, you will need to provide the stylesheet of the website that hides the tailwind classes (`-c` flag).

### CLI

Just give you r input after the `-r` flag.

```shell
retailwind -c style.css -r yz
```

### Interactive

Use the `-i` flag, it will start the interactive app.

```shell
retailwind -c style.css -i
```

![app](/assets/retailwind.png)

You can write (or paste through shift+right-click or your terminal shortcut like ctrl+shift+v) html fragments and see the translated version on the right panel.

### Library

```python
from retailwind.translator import Translator

# init the translator with the stylesheet
tr = Translator("/path/to/styles.css")
# run on raw class
tr.raw("yz")
# run on html fragment
tr.html("<div class='kw lx yz aai'>retailwind</div>")
```
