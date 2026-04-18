import os

root = '../project102'
os.makedirs(root,exist_ok=True)

os.chdir(root)


# 创建多层文件
dir_name = [
    'eda/figures',
    'inputs',
    'outputs',
    'param_tuning',
    'results/figures',

]

# 创建文件必须带.py等文件类型
files = [
    ".gitignore",
    "Dockerfile",
    "README.md",
    "requirements.txt",
    "main.py",
    "main_train.py",
    "test_model.py",
    "eda/eda_house_price.ipynb",
    "param_tuning/optuna_tuning.ipynb",
    "param_tuning/manual_tuning.ipynb"
]

for d in dir_name:
    os.makedirs(d,exist_ok=True)

for f in files:
    with open(f,'w',encoding='utf-8') as fp:
        pass

print("W")

