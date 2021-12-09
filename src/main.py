# coding: utf-8
import os
import sys
try:
    src_dir = os.path.dirname(__file__)
except Exception:
    src_dir = r'D:\Development\Programming\Revit\IronPython\revit-api-stubs\src'
    if not os.path.exists(src_dir):
        raise ValueError('Некорректный путь к папке src')

root_dir = os.path.dirname(src_dir)
sys.path.extend([root_dir, src_dir])
os.chdir(root_dir)  # Для того чтобы логгер нашёл корневую папку

from make_stubs import crawl_loaded_references, create_stubs

stubs_dir = os.path.join(
    root_dir, 'stubs', 'revit', __revit__.Application.VersionNumber  # type: ignore
)

for assembly_name in ['RevitAPI', 'RevitAPIUI']:
    assembly = crawl_loaded_references(assembly_name)
    for modules in assembly.values():
        for namespace in modules.keys():
            create_stubs(stubs_dir, namespace)
