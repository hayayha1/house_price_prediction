import os
import shutil
from pathlib import Path


# 复制d盘的数据集到c盘的inputs目录
root = Path((os.getcwd())).parent

src_1 = 'D:/train.csv'
src_2 = 'D:/test.csv'

shutil.copy(src_1, root / 'inputs' / 'train.csv')
shutil.copy(src_2,root/ 'inputs'  /'test.csv')

