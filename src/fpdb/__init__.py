from .forked_pdb import ForkedPdb

__version__ = "0.0.1dev0"
# __author__ = "Your Name"
__license__ = "Apache-2.0"
__status__ = "Development"
__description__ = "A Python package for debugging multi-processed code using PDB."
__keywords__ = ["debugging", "pdb", "multiprocessing"]
# __long_description__ = """
# ForkedPdb is a Python package that provides a subclass of the built-in PDB debugger,
# allowing you to debug multi-processed code. It overrides the interaction method to
# handle standard input correctly in a multi-process environment.
# """
# __long_description_content_type__ = "text/markdown"
__all__ = ["ForkedPdb"]
