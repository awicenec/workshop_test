__package__ = "workshop_test"
# The following imports are the binding to the DALiuGE system
from dlg import droputils, utils

# extend the following as required
from .apps import MyAppDROP
from .data import MyDataDROP

__all__ = ["MyAppDROP", "MyDataDROP"]
