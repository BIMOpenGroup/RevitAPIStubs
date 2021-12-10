"""Базовый пример с не определённым типом для переменной цикла el.
"""

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit import DB
from rps import doc  # перед запуском надо закомментировать

views = DB.FilteredElementCollector(doc) \
    .OfClass(DB.View3D) \
    .WhereElementIsElementType()

for el in views:
    print(el)
