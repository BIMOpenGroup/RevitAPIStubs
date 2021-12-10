"""Определение типа переменной цикла обозначив тип для последовательности.

Можно сделать приведение к более общему типу, так как
View3D наследник View, а View наследник Element.
Но будьте осторожны, не ошибитесь в выборе базового типа.
"""

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit import DB
from rps import doc  # перед запуском надо закомментировать

views = DB.FilteredElementCollector(doc) \
    .OfClass(DB.View3D) \
    .WhereElementIsNotElementType() \
    .ToElements()  # type: list[DB.Element]

for el in views:
    print(el.Name)
