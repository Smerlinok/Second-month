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
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __eq__(self, other):
        return self.__cpu == other.cpu and self.__memory == other.memory

    def __ne__(self, other):
        return self.__cpu != other.cpu or self.__memory != other.memory

    def __lt__(self, other):
        return self.__cpu < other.cpu and self.__memory < other.memory

    def __gt__(self, other):
        return self.__cpu > other.cpu and self.__memory > other.memory

    def __le__(self, other):
        return self.__cpu <= other.cpu and self.__memory <= other.memory

    def __ge__(self, other):
        return self.__cpu >= other.cpu and self.__memory >= other.memory


    def make_computations(self):
        addition = self.__cpu + self.__memory
        multiplication = self.__cpu * self.__memory
        print(f"Addition of cpu and memory: {addition}, multiplication: {multiplication}")

    def __str__(self):
        return f'Информация об объекте - cpu: {self.__cpu}, memory: {self.__memory}'

class Phone:
    def __init__(self, sim_cards_list ):
       self.__sim_cards_list = sim_cards_list
       
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
       
    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number < 1 or sim_card_number > len(self.__sim_cards_list):
            print("Нет информации")
        else:
            sim_card = self.__sim_cards_list[sim_card_number - 1]

        operator_dict = {
            'Beeline': 'Beeline',
            'O!': 'O!',
            'Mega': 'Mega'}

        operator = operator_dict.get(sim_card, 'Неизвестный оператор')

        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} ({operator})")

    def __str__(self):
        return f'Информация об объекте - sim_card: {self.__sim_cards_list} '



class Smartphone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print( f'Маршрут построен до {location} ')

    def __str__(self):
        return f'Информация об объекте: cpu: {self.cpu}, memory: {self.memory}, sim_cards: {self.sim_cards_list}'

computer = Computer(cpu=4, memory=6)
phone = Phone(sim_cards_list=['Beeline', 'O!', 'Mega'])
smartphone = Smartphone(cpu= 5, memory= 8, sim_cards_list=['Beeline', 'Mega'])
smartphone2 = Smartphone(cpu=6, memory=7, sim_cards_list=['Beeline', 'Mega'])

print(computer)
print(phone)
print(smartphone)
print(smartphone2)

computer.make_computations()
phone.call(1, +996550050505)
phone.call(2, +996564783466)
smartphone.use_gps('Город')

print(smartphone==smartphone2)
print(smartphone<smartphone2)
print(smartphone>smartphone2)
print(smartphone<=smartphone2)
print(smartphone>=smartphone2)
print(smartphone!=smartphone2)

