import time
import matplotlib.pyplot as plt
import memory_profiler


class binary:

    def __init__(self):

        self.elapsed_times = []
        self.memory_usages = []
        self.index = []

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Recording time and memory at each iteration
            start_time = time.time()
            memory_used = memory_profiler.memory_usage()[0]

            if arr[mid] == target:
                # Handle all occurrences of the target to the left
                left = mid
                while left >= 0 and arr[left] == target:
                    self.index.append(left)
                    left -= 1

                # Handle all occurrences of the target to the right
                right = mid + 1
                while right < len(arr) and arr[right] == target:
                    self.index.append(right)
                    right += 1

                # Recording time and memory at each iteration
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.elapsed_times.append(elapsed_time)
                self.memory_usages.append(memory_used)

                return self.index

            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            # Recording time and memory at each iteration
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.elapsed_times.append(elapsed_time)
            self.memory_usages.append(memory_used)

        return self.index

    # Rest of your class remains unchanged

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
