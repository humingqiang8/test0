def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    # 创建数组的副本，避免修改原数组
    n = len(arr)
    arr = arr.copy()
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮排序后，最大的元素会"冒泡"到末尾
        # 所以内层循环的范围可以逐渐减小
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_with_steps(arr):
    """
    带步骤显示的冒泡排序，用于演示排序过程
    """
    print(f"原始数组: {arr}")
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        swapped = False
        print(f"\n第 {i+1} 轮排序:")
        
        for j in range(0, n - i - 1):
            print(f"  比较 {arr[j]} 和 {arr[j+1]}", end="")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f" -> 交换: {arr}")
            else:
                print(f" -> 不交换: {arr}")
        
        if not swapped:
            print("  没有发生交换，排序完成")
            break
    
    print(f"\n最终结果: {arr}")
    return arr


# 测试冒泡排序
if __name__ == "__main__":
    # 测试用例
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],  # 单个元素
        [],   # 空数组
        [1, 2, 3, 4, 5],  # 已排序数组
        [5, 4, 3, 2, 1]   # 逆序数组
    ]
    
    print("=== 冒泡排序测试 ===")
    for i, arr in enumerate(test_arrays):
        original = arr.copy()
        sorted_arr = bubble_sort(arr)
        print(f"测试 {i+1}: {original} -> {sorted_arr}")
    
    print("\n=== 排序过程演示 ===")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_with_steps(demo_array)