from code.Entity import Entity


class Background (Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        print(f"Background {self.name} carregado na posição {self.rect.topleft}")

    def move(self, ):
        pass
