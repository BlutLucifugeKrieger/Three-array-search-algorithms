import time
import matplotlib.pyplot as plt
import memory_profiler


class linear:

    def __init__(self):
        self.elapsed_times = []
        self.memory_usages = []
        self.index = []

    def search(self, array, objective):
        
         start_time = time.time()
        
        for i in range(len(array)):
           
            if array[i] == objective:
                self.index.append(i)
                end_time = time.time()
                elapsed_time = end_time - start_time
                memory_used = memory_profiler.memory_usage()[0]

                self.elapsed_times.append(elapsed_time)
                self.memory_usages.append(memory_used)

    def objective_index(self, objective):

        if self.index:

            return f"The number {objective} is in the array at index: {self.index}"

        else:

            return f"The number {objective} wasn't in the array"

    def single_value(self):
        len_index = len(self.index)

        if len_index == 1:
            value_time = self.elapsed_times[0]
            value_memory = self.memory_usages[0]
            for _ in range(5):
                self.elapsed_times.append(value_time)
                self.memory_usages.append(value_memory)

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
