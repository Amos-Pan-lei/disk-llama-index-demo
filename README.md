## 前置准备
> python环境要求 版本>=3.9.0

### 安装依赖

```shell
pip3 install -r openai llama-index tiktoken
```

 

 

## 运行


#### 在代码中填入API key，或者设置环境变量


##### win环境

```powershell
$env:OPENAI_API_KEY="api-key"
```

#### 建立索引

```shell
python3 build_index.py
```

#### 查询索引

```shell
python3 query_index.py
```