import os # operating system

def read_file(filename):
    products =[]
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #跳到下一個loop, 不會離開loop 
            name, price = line.strip().split(',')   #先進行remove \n ;在進行split功能 切割完的結果是清單
            products.append([name, price])
    return products
               
#讓使用者輸入
def user_input(products):
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
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        #print(p)
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: #utf-8編碼 中文字
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')



def main():
    filename = 'products.csv'
    if os.path.isfile(filename):    # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案喔!!!')
        
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()
