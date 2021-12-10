"""Определение типа переменной цикла через инициализацию переменной до цикла.

На код это не сильно повлияет, так как переменная цикла всё равно создаётся в
глобальной области видимости и нет ничего страшного что ей сначала присваевается тип.
Заметьте, если убрать комментарий, то Pylance не сможет определить тип для переменной цикла.
"""

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit import DB
from rps import doc  # перед запуском надо закомментировать

views = DB.FilteredElementCollector(doc) \
    .OfClass(DB.View3D) \
    .WhereElementIsNotElementType()

view = DB.View3D  # type: DB.View3D
for view in views:
    # Свойство ViewName является устаревшим и не поддерживается в RevitAPI начиная с 2020 версии.
    # Можете это проверить переключив заглушки для данного проекта
    print(view.ViewName)
