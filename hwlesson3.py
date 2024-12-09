class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

        @property
        def cpu(self):
            return self.__cpu

        @cpu.setter
        def cpu(self, value):
            self.__cpu = value

        @property
        def memory(self):
            return memory

        @memory.setter
        def memory(self, value):
            self.__memory = value

    def make_computations(self):
        addition = self.__cpu + self.__memory
        multiplication = self.__cpu * self.__memory
        print(f"Addition of cpu and memory: {addition}, multiplication: {multiplication}")
