Template Rendering Tool
=======================

A tool to render [Jinja2](http://jinja.pocoo.org/docs/dev/) templates using the command line interface or environment variables. This tool is useful when templating complex configuration files and matching text with sed is a nightmare!

**Install using pip:**
```
$] sudo pip install trt
```

**Install using setuptools:**
```
$] git clone https://github.com/thomasquintana/trt.git
$] cd trt
$] python setup.py install
```

**Usage:**
```
$] trt -h
usage: trt [-h] -s SOURCE -d DESTINATION -ps {environment,cli}
           [-p [PARAMETERS [PARAMETERS ...]]]

Renders a [Jinja2](http://jinja.pocoo.org/docs/dev/) template using command line arguments or environment
variables as parameters for the template.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE             The path to the source template.
  -d DESTINATION        The path to the destination file.
  -ps {environment,cli}
                        The source of the parameters for the template. The
                        options are 'environment' if you want to use the
                        environment variables as parameters or 'cli' if you
                        want to pass in the parameters as arguments to this
                        script. Note: All parameter names are converted to
                        lower case irrelevant of the parameters source.
  -p [PARAMETERS [PARAMETERS ...]]
                        A parameter to pass into the template renderer if the
                        parameters-source is 'cli'.
```