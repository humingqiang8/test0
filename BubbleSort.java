public class BubbleSort {
    
    /**
     * 冒泡排序算法实现
     * @param arr 待排序的整数数组
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        // 外层循环控制排序轮数
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false; // 优化：如果某一轮没有发生交换，说明数组已经有序
            
            // 内层循环进行相邻元素比较和交换
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // 交换 arr[j] 和 arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            
            // 如果这一轮没有发生交换，数组已经有序，可以提前结束
            if (!swapped) {
                break;
            }
        }
    }
    
    /**
     * 打印数组元素
     * @param arr 要打印的数组
     */
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }
    
    /**
     * 主方法 - 测试冒泡排序
     */
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("原始数组:");
        printArray(arr);
        
        bubbleSort(arr);
        
        System.out.println("排序后数组:");
        printArray(arr);
        
        // 测试已经排序的数组（验证优化效果）
        int[] sortedArr = {1, 2, 3, 4, 5};
        System.out.println("\n测试已排序数组:");
        System.out.println("原始数组:");
        printArray(sortedArr);
        
        bubbleSort(sortedArr);
        
        System.out.println("排序后数组:");
        printArray(sortedArr);
    }
}