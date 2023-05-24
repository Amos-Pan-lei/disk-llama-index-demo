import logging
import sys
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex 

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

 
# 读取data文件夹下的文档
documents = SimpleDirectoryReader('data').load_data()
# 按最大token数500来把原文档切分为多个小的chunk，每个chunk转为向量，并构建索引
 

index = GPTVectorStoreIndex.from_documents(documents)

# 保存索引
index.storage_context.persist(persist_dir='./index/mks')


