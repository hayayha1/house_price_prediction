from fastapi import FastAPI
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

# 加载训练时保存的所有对象
model = pickle.load(open("outputs/model.pkl", "rb"))
encoder = pickle.load(open("outputs/encoder.pkl", "rb"))

train = pd.read_csv('inputs/train.csv')
cat_cols = train.select_dtypes(include='str').columns.tolist()

@app.post("/predict")
def predict(data: dict):
    try:
        # 1. 把接口传入的JSON转成DataFrame
        df = pd.DataFrame([data])

        # 2. 处理分类特征（和训练时完全一样）
        df_cat = df[cat_cols]
        df_cat_encoded = encoder.transform(df_cat)
        encoded_df = pd.DataFrame(df_cat_encoded, columns=encoder.get_feature_names_out(cat_cols))
        df = df.drop(cat_cols, axis=1)
        df_processed = pd.concat([df, encoded_df], axis=1)



        pred = model.predict(df_processed)


        return {"预测房价": pred[0]}

    except Exception as e:
        return {"错误": str(e)}

