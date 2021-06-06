#二維清單
#讀取檔案
products =[]
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue #跳到下一個loop, 不會離開loop 
        name, price = line.strip().split(',')   #先進行remove \n ;在進行split功能 切割完的結果是清單
        products.append([name, price])        
print(products)

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price)
    p = [name, price]
    products.append(p)   #products.append([name, price]) 
print(products)

# 印出所有購買紀錄
for p in products:
    print(p)
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #utf-8編碼 中文字
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

