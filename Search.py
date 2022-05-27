def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    low = 0 #　先頭のインデックス
    high = len(sorted_array) - 1 # 最後尾のインデックス

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid] # 中間の値の更新

        if guess == target_number: # 探索対象と中間の値が一致
            return mid
        if guess > target_number:
            high = mid - 1
        else:
            low = mid + 1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却 
    return -1

if __name__ == '__main__':
    main()