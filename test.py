from vec import Vec
import collections
# import codon
import random
import time

class RollingMedianCodon:
    n: int 
    data: collections.deque[float]

    def __init__(self, n: int = 10):
        self.n = n
        self.data = collections.deque(maxlen=n)

    
    def input(self, value: float):
        self.data.append(value)
        return self.get_median()
        
    # @codon.jit
    def get_median(self):
        sorted_data = sorted(self.data)
        mid = len(sorted_data) // 2

        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

class RollingMedian:
    n: int 
    data: collections.deque[float]

    def __init__(self, n: int = 10):
        self.n = n
        self.data = collections.deque(maxlen=n)

    def input(self, value: float):
        self.data.append(value)
        return self.get_median()
        
    def get_median(self):
        sorted_data = sorted(self.data)
        mid = len(sorted_data) // 2

        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]


def test_performance():
    # 创建两个实例
    rolling_median_jit = RollingMedianCodon(n=20)
    rolling_median_normal = RollingMedian(n=20)
    
    # 生成测试数据
    test_data = [random.uniform(0, 1000) for _ in range(100000)]
    
    # 测试JIT版本
    start_time = time.time()
    for value in test_data:
        rolling_median_jit.input(value)
    jit_time = time.time() - start_time
    
    # 测试普通版本
    start_time = time.time()
    for value in test_data:
        rolling_median_normal.input(value)
    normal_time = time.time() - start_time
    
    print(f"JIT Version: {jit_time:.4f}秒")
    print(f"Normal Version: {normal_time:.4f}秒")
    print(f"Performance Inprovement {(normal_time/jit_time - 1)*100:.2f}%")

if __name__ == "__main__":
    test_performance()

