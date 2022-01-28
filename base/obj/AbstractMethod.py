from abc import ABC,abstractmethod
# 抽象类
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

# 直接实例化抽象类报错
t=Talker()
