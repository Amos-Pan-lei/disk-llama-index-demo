import logging
import sys
from llama_index import StorageContext, load_index_from_storage

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# 加载索引

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./index/mks")

# load index
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

while True:
    user_input = input("请输入文本：")
        # 非空校验
    if not user_input:
        print("输入的内容不能为空，请重新输入！")
        continue
    # 在这里处理用户输入并输出响应
    print("您输入了：" + user_input)
    # 查询索引
    response = query_engine.query(user_input)
    # 打印答案
    print(response)
    if user_input == "退出":
        print("再见！")
        break

