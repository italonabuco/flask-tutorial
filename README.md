# Flask Tutorial

## Install Pipenv

Pipenv is a dependency manager for Python projects. If you’re familiar with Node.js’ npm or Ruby’s bundler, it is similar in spirit to those tools.

Use pip to install Pipenv:

```shell
$ pip install --user pipenv
```

If pipenv isn’t available in your shell after installation, you’ll need to add the user base’s binary directory to your PATH.

```
$ python -m site --user-base
```

And adding bin to the end. For example, this will typically print ~/.local (with ~ expanded to the absolute path to your home directory) so you’ll need to add ~/.local/bin to your PATH.
