def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # i番目の値と基準値を比較して左l、右r、真ん中cに追加してゆく
    l = []
    r = []
    c = []
    for i in range(len(array)):
        sample = array[i]
        if sample < pivot:
            l.append(sample)
        elif sample > pivot:
            r.append(sample)
        else:
            c.append(sample)
    # lとrの場合でそれぞれ再帰処理による分割を行う
    if l:
        l = sort(l)
    if r:
        r = sort(r)
    return l + c + r # それぞれソートされた3つの配列をつなげる
    # ここまで記述

if __name__ == '__main__':
    main()