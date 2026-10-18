## □ 查看變數型別(Variable Type)
使用 type() 函數可以檢查物件類型 加上 __name__ 成員會傳回屬性的名稱

讓我們檢查學過的字串型別!:
```
s = input()
print(type(s)) # 檢查物件的類型，因此該語句會輸出：<class 'str'>
print(type(s).__name__) # 因為 __name__ 會傳回屬性的名稱，所以語句會輸出：str
```

## □ 整數型態(Integer) 與浮點數(Float)
int 表態的通常是十進位整數。
值得注意的是:
Python 的 int 型別沒有像 C 語言那樣的固定大小限制。

int() 函數：
此函數會將非整數型態物件轉換為整數

範例:
```
d = int(input())
print(type(d).__name__) # 該語句會輸出：int
```

float ，可以將其視為小數。
與 C 家族不同，Python 可容納的精度極大。

float() 函數：
此函數會將物件轉換為浮點數

範例:
```
d = float(input())
print(type(d).__name__) # 此語句會輸出：float
```

### □ int() 引申操作
以下為該函數的詳細示意:
```
int([object], [Bases])
```

Bases 預設為 10
誠如方才所演示
假設輸入字串行別的 10 經過 `int(input())` 並賦值操作之後
將會得到整數型別的 10

如果要將二進位轉換回十進位 就將 Bases 設為 2

範例:
```
print(int("0b0110", 2))
```
0b 前綴(prefix) 可打可不打。
有關前綴，這個之後再了解就可以。

## □ print() 引申操作
以下為對 print() 函數預設的參數進行更動的範例:
```
print(1, 2, 3, 4, 5, sep=" ", end="\n") # 預設行為：元素間以空格分隔，並以換行符號結尾
print(1, 2, 3, 4, 5, sep="") # 元素之間沒有分隔符
print(1, 2, 3, 4, 5, sep=" ", end="") # 輸出末端沒有換行符
```
