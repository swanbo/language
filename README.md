# 项目用途
- 方便背单词
- 学习编程知识
- 收获Star
# 单词数据结构
```python
# word
{
    'id': 1, # 单词编号
    'spell': 'abandon', # 拼写
    'pron': '[əˈbændən]', # 音标
    'en': 'o leave sb, especially sb you are responsible for', # 英语意思
    'zh': '抛弃', # 中文意思
    'sentence_id': '例句id', # 一对多
    'origin': '来源', # 比如是学编程的时候看到的，看剧的时候看到的
    'tag': '标签', # 单词分类
    'remark': '备注',
    'refs': '相关单词' # 同义词，反义词，联想到的词 多对多的关系
}

# sentence
{
    'id': 1, # 句子编号
    'text': "句子内容",
    'origin': '句子来源'
}
```
# 开发进度
- 20220610 实现单词的简单后台数据结构

# TODO
- 根据单词自动获取音标和发音
- 可以根据熟悉程度来决定颜色
- 导出单词
- 单词标签(四六级，考研，雅思，人教版一年级上， etc.)
- 最好是能在网页上调用某个词典的接口，这样发音和释义就都有了
# 附录
## 原理
利用excel重复快速大量浏览单词达到记忆效果
## bug记录
没有在setting.py中注册app是执行migrate操作不会去创建对应app的数据库表
