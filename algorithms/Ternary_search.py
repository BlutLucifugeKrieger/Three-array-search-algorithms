
import time
import matplotlib.pyplot as plt
import memory_profiler



class ternary:

    def __init__(self):
        self.elapsed_times = []
        self.memory_usages = []
        self.index = []

    def ternary_search(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            third_1 = start + (end - start) // 3
            third_2 = end - (end - start) // 3
            start_time = time.time()
            memory_used = memory_profiler.memory_usage()[0]

            if arr[third_1] == target:
                self.index.append(third_1)
                start = third_1 + 1
            elif arr[third_2] == target:
                self.index.append(third_2)
                end = third_2 - 1
            elif target < arr[third_1]:
                end = third_1 - 1
            elif target > arr[third_2]:
                start = third_2 + 1
            else:
                start = third_1 + 1
                end = third_2 - 1

            end_time = time.time()
            elapsed_time = end_time - start_time
            self.elapsed_times.append(elapsed_time)
            self.memory_usages.append(memory_used)


    def objective_index(self, objective):

        if len(self.index) > 0:

            return f"The number {objective} is in the array at index: {self.index}"

        else:

            return f"The number {objective} wasn't in the array"

    # pragma: no cover
    def plot_graphs(self): # pragma: no cover

        len_index = len(self.index)

        if len_index != 0:
            # graph time and memory
            plt.figure(figsize=(10, 5))

            # time graph
            plt.subplot(2, 1, 1)
            plt.plot(self.elapsed_times, label='Elapsed Time')
            plt.xlabel('Iteration')
            plt.ylabel('Time (seconds)')
            plt.title('Elapsed Time in Each Iteration')
            plt.legend()

            # memory graph
            plt.subplot(2, 1, 2)
            plt.plot(self.memory_usages, label='Memory Used')
            plt.xlabel('Iteration')
            plt.ylabel('Memory (MB)')
            plt.title('Memory Used in Each Iteration')
            plt.legend()

            plt.tight_layout()
            plt.show()

        else:
            print(f"Please, try again")