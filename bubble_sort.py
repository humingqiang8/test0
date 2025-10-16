def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
    arr: 待排序的列表
    
    返回:
    排序后的列表
    """
    n = len(arr)
    
    # 遍历所有数组元素
    for i in range(n):
        # 标记是否发生了交换，用于优化
        swapped = False
        
        # 最后i个元素已经排好序了
        for j in range(0, n - i - 1):
            # 如果当前元素比下一个元素大，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经排序完成
        if not swapped:
            break
    
    return arr


def bubble_sort_with_steps(arr):
    """
    带步骤显示的冒泡排序算法实现
    
    参数:
    arr: 待排序的列表
    
    返回:
    排序后的列表
    """
    n = len(arr)
    print(f"初始数组: {arr}")
    
    for i in range(n):
        swapped = False
        print(f"\n第 {i + 1} 轮排序:")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"  交换 {arr[j]} 和 {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print(f"  不交换 {arr[j]} 和 {arr[j + 1]}")
        
        print(f"  第 {i + 1} 轮结果: {arr}")
        
        if not swapped:
            print("  没有发生交换，排序完成")
            break
    
    return arr


# 测试冒泡排序
if __name__ == "__main__":
    # 测试用例1
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("测试用例 1:")
    print(f"排序前: {test_arr1}")
    sorted_arr1 = bubble_sort(test_arr1.copy())
    print(f"排序后: {sorted_arr1}")
    
    print("\n" + "="*50 + "\n")
    
    # 测试用例2
    test_arr2 = [5, 2, 8, 1, 9]
    print("测试用例 2 (带步骤):")
    bubble_sort_with_steps(test_arr2)
    
    print("\n" + "="*50 + "\n")
    
    # 测试用例3：已排序数组
    test_arr3 = [1, 2, 3, 4, 5]
    print("测试用例 3 (已排序数组):")
    print(f"排序前: {test_arr3}")
    sorted_arr3 = bubble_sort(test_arr3.copy())
    print(f"排序后: {sorted_arr3}")
    
    print("\n" + "="*50 + "\n")
    
    # 测试用例4：逆序数组
    test_arr4 = [5, 4, 3, 2, 1]
    print("测试用例 4 (逆序数组):")
    print(f"排序前: {test_arr4}")
    sorted_arr4 = bubble_sort(test_arr4.copy())
    print(f"排序后: {sorted_arr4}")