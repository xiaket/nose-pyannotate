# nose-pyannotate

This is a simple plugin for [nose](https://pypi.org/project/nose/) that glue the internal hooks provided by nose with [pyannotate](https://pypi.python.org/pypi/pyannotate) so we can generate the `type_info.json` file by running `nosetests`.


# Installation and usage

The installation is plain, just use pip to install it.

```
pip install nose-pyannotate
```

After the installation, the plugin will auto-register itself with nose. So if you run:

```
nosetests -p --verbosity=2
```

You'll be able to find this plugin among many others:

```
Plugin nose-pyannotate
  score: 100
  Write `type_info.json` file using pyannotate, for pyannotate.
```

Finally, run nose with the following flag to enable this plugin:

```
nosetests --with-nose-annotate
```
