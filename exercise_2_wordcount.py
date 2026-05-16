# exercise_2_wordcount.py
# 文本词频统计器

# 1. 获取用户输入
text = input("请输入一段文字：")

# 2. 转小写
text = text.lower()

text = text.replace(",", " ").replace(".", " ")

# 3. 拆成单词列表
words = text.split()

# 4. 统计每个单词的次数
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# 5. 按次数从高到低排序
sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# 6. 输出结果
for word, count in sorted_items:
    print(f"{word}: {count}") 