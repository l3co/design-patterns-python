from abc import ABC, abstractmethod


class Compiler(ABC):
    @abstractmethod
    def collect_source(self): pass

    @abstractmethod
    def compile_to_object(self): pass

    @abstractmethod
    def run(self): pass

    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()
