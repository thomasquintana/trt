# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Thomas Quintana <quintana.thomas@gmail.com>

import os

from argparse import ArgumentParser

from jinja2 import Environment, FileSystemLoader

def to_lowercase_keys(parameters):
  if isinstance(parameters, list):
    return {k.lower(): v for k, v in [p.split("=") for p in parameters]}
  elif isinstance(parameters, dict):
    return {k.lower(): v for k, v in parameters.iteritems()}
  else:
    raise ValueError("Invalid type for parameters.")

def split_path(path):
  split_point = path.rfind("/")
  if not split_point == -1:
    return path[:split_point], path[split_point + 1:]
  else:
    return None, path

if __name__ == "__main__":
  PARSER = ArgumentParser(
    description="Renders a Jinja2 template using command line arguments or " +
                "environment variables as parameters for the template."
  )
  PARSER.add_argument(
    "-s", dest="SOURCE", required=True,
    help="The path to the source template."
  )
  PARSER.add_argument(
    "-d", dest="DESTINATION", required=True,
    help="The path to the destination file."
  )
  PARSER.add_argument(
    "-ps", dest="PARAMETER_SOURCE", choices=["environment", "cli"], required=True,
    help="The source of the parameters for the template. The options " +
         "are 'environment' if you want to use the environment variables " +
         "as parameters or 'cli' if you want to pass in the parameters " +
         "as arguments to this script. Note: All parameter names are " +
         "converted to lower case irrelevant of the parameters source."
  )
  PARSER.add_argument(
    "-p", dest="PARAMETERS", nargs="*", required=False,
    help="A parameter to pass into the template renderer if the " +
         "parameters-source is 'cli'."
  )
  ARGS = PARSER.parse_args()
  # Load the parameters.
  PARAMETERS = None
  if ARGS.PARAMETER_SOURCE == "cli":
    PARAMETERS = ARGS.PARAMETERS
  elif ARGS.PARAMETER_SOURCE == "environment":
    PARAMETERS = dict(os.environ)
  PARAMETERS = to_lowercase_keys(PARAMETERS)
  # Load the templates.
  FOLDER_NAME, FILE_NAME = split_path(ARGS.SOURCE)
  LOADER = FileSystemLoader(FOLDER_NAME)
  TEMPLATES = Environment(loader=LOADER)
  # Render the template.
  TEMPLATE = TEMPLATES.get_template(FILE_NAME).render(PARAMETERS)
  # Write the rendered template to disk.
  with open(ARGS.DESTINATION, "wb") as output:
    output.write(TEMPLATE)
