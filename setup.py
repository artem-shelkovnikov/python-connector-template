import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    raise ValueError("Requires Python 3.6 or superior")

from python_connector_template import __version__  # NOQA

install_requires = [
    "elastic_enterprise_search",
    "pyyaml",
    "tika",
    "ecs_logging"
]

description = ""

for file_ in ("README", "CHANGELOG"):
    with open("%s.rst" % file_) as f:
        description += f.read() + "\n\n"


classifiers = [
    "Programming Language :: Python",
    "License :: OSI Approved :: Apache Software License",
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]


setup(
    name="python connector template",
    version=__version__,
    url="https://example.com",
    packages=find_packages(),
    long_description=description.strip(),
    description=("This is a template python project for a Enterprise Search Connector."),
    author="author",
    author_email="email",
    include_package_data=True,
    zip_safe=False,
    classifiers=classifiers,
    install_requires=install_requires,
    entry_points="""
      [console_scripts]
      bootstrap=python_connector_template.cmd:bootstrap
      check_connectivity=python_connector_template.cmd:check_connectivity
      full_sync=python_connector_template.cmd:full_sync
      incremental_sync=python_connector_template.cmd:incremental_sync
      deletions_sync=python_connector_template.cmd:deletion_sync
      """,
)
