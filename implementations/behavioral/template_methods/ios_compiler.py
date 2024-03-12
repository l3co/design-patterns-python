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


class IOsCompiler(Compiler):
    def collect_source(self):
        print("Collecting swift source code")

    def compile_to_object(self):
        print("Compiling swift code to LLVM bitcode")

    def run(self):
        print("Program running on runtime environment")


if __name__ == '__main__':
    ios_compiler = IOsCompiler()
    ios_compiler.compile_and_run()
