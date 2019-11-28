# 使用Python copy一个文件，从a目录,copy文件到b目录

import os
from pathlib import Path
import shutil

src_path=Path('a/test')
dst_path=Path('b/test')

with open(src_path,'w') as src_file:
    src_file.write('abcd\n1234')

shutil.copy(src_path,dst_path)

print(os.stat(src_path))
print(os.stat(dst_path))