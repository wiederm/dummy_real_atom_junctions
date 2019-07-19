"""
ghost_parameters
Transforms a topology and parameter with dummy atoms in such a way that the dummy group does not influence the geometry of the real atoms.
"""

# Add imports here
from .ghost_parameters import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
