from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        raise NotImplementedError

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError

class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError

class IVIP:
    def validar_usuario_vip(self,usuario):
        raise NotImplementedError

class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1

class DescontoVip(IDesconto):
    def calcular(self, valor):
        return valor * 0.2

class DescontoPremium(IDesconto):
    def calcular(self, valor):
        return valor * 0.3
    
class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)

def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)

if __name__ == "__main__":
    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVip())

    print("Normal:", pedido_normal.total(valor))
    print("VIP:", pedido_vip.total(valor))

"""def main():
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVip()
    premium = DescontoPremium()

    print(f"Desconto Normal: R$ {normal.calcular(valor):.2f}")
    print(f"Desconto VIP: R$ {vip.calcular(valor):.2f}")
    print(f"Desconto Premium: R$ {premium.calcular(valor):.2f}")"""