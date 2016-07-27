Template Rendering Tool
=======================

A tool to render templates using the command line interface or environment variables. This tool is useful when templating complex configuration files and matching text with sed is a nightmare!

**Install:**
```
$] git clone https://github.com/thomasquintana/trt.git
$] cd trt
$] python setup.py install
```

**Usage:**
```
$] python tool.py --help
usage: tool.py [-h] --source SOURCE --destination DESTINATION
               --parameters-source {environment,cli}
               [--parameter [PARAMETER [PARAMETER ...]]]

Renders a Jinja2 template using command line arguments or environment
variables as parameters for the template.

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       The path to the source template.
  --destination DESTINATION
                        The path to the destination file.
  --parameters-source {environment,cli}
                        The source of the parameters for the template. The
                        options are 'environment' if you want to use the
                        environment variables as parameters or 'cli' if you
                        want to pass in the parameters as arguments to this
                        script. Note: All parameter names are converted to
                        lower case irrelevant of of the parameters source.
  --parameter [PARAMETER [PARAMETER ...]]
                        A parameter to pass into the template renderer if the
                        parameters-source is 'cli'.
```