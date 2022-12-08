import csv
import pandas as pd

# 将csv文件内数据读出
with open('paper0.csv', 'r', encoding="utf-8") as f1, open(
        'paper.csv', 'a', newline='', encoding="utf-8") as f3:
    # 生成csv操作对象
    reader1 = csv.reader(f1)
    writer = csv.writer(f3)
    df = pd.read_csv('paper.csv', header=None, names=['title', 'author', 'publication_date', 'abstract', 'link'])
    df.to_csv('paper.csv', index=False)
    with open('abstract0.csv', 'r', encoding="utf-8") as f2:
        reader2 = csv.reader(f2)
        author_list = [row[0] for row in reader2]
    with open('abstract0.csv', 'r', encoding="utf-8") as f2:
        reader2 = csv.reader(f2)
        abstract_list = [row[1] for row in reader2]
    with open('abstract0.csv', 'r', encoding="utf-8") as f2:
        reader2 = csv.reader(f2)
        index_list = [row[2] for row in reader2]
    count = 1
    for row1 in reader1:
        title = row1[0]
        link = row1[1]
        publication_date = row1[2]
        author = ''
        abstract = ''
        for i in range(len(index_list)):
            if index_list[i] == str(count):
                author = author_list[i]
                abstract = abstract_list[i]
                break
        if author != '':
            row = [title, author, publication_date, abstract, link]
            writer.writerow(row)
        count = count + 1
        if count >= 16000:
            break
