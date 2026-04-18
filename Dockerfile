# 基础 Python 镜像（稳定、轻量）
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 把项目所有文件复制到容器里
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 FastAPI 端口（和你代码一致）
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
