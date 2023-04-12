import logging
import sys
from llama_index import GPTSimpleVectorIndex

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# 加载索引
new_index = GPTSimpleVectorIndex.load_from_disk('index.json')

while True:
    user_input = input("请输入文本：")
        # 非空校验
    if not user_input:
        print("输入的内容不能为空，请重新输入！")
        continue
    # 在这里处理用户输入并输出响应
    print("您输入了：" + user_input)
    # 查询索引
    response = new_index.query(user_input)
    # 打印答案
    print(response)
    if user_input == "退出":
        print("再见！")
        break

