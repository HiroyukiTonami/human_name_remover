import MeCab
import csv
import os
t = MeCab.Tagger()

def search_target_paths(path):
    target = []
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.csv'):
                target.append((filename[:-4], os.path.join(pathname,filename)))

    return target

def name_remove(text):
    node = t.parseToNode(text)
    ret_text = ''
    while node:
        word = node.surface
        wclass = node.feature.split(',')
        if wclass[0] != u'BOS/EOS':
            if wclass[2] == '人名':
                text = text.replace(word, '人名')
        node = node.next

    return text


def main():
    target = search_target_paths(os.getcwd())
    for filename, fp in target:
        with open(fp, "r", newline="" ,encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            new_csv = []
            for row in reader:
                new_row = ['']*len(row)
                for i, column in enumerate(row):
                    new_row[i] = name_remove(column)
                new_csv.append(new_row)
        with open(f'{filename}_result.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(new_csv)

main()
