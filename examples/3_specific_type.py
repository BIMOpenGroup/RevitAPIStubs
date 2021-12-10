"""Определение типа переменной цикла обозначив тип для последовательности.

Это выглядит более органично, хоть и добавляет вызов не обязательного метода ToElements.
"""

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit import DB
from rps import doc  # перед запуском надо закомментировать

views = DB.FilteredElementCollector(doc) \
    .OfClass(DB.View3D) \
    .WhereElementIsNotElementType() \
    .ToElements()  # type: list[DB.View3D]

for view in views:
    # Свойство ViewName является устаревшим и не поддерживается в RevitAPI начиная с 2020 версии.
    # Можете это проверить переключив заглушки для данного проекта
    print(view.ViewName)
