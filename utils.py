from decimal import Decimal

class Engine:
    def init(self, body) -> None:
        self.body = self.format_body(body)

    @classmethod
    def format_body(cls, body: str) -> Decimal:
        '20.1'

        c = Decimal(body).quantize(Decimal('1.0'))
        
        return str(c)

    def str(self):
        return self.body


class EngineTwo:
    def init(self, body) -> None:
        self.body = self.format_body(body)

    @classmethod
    def format_body(cls, body: str) -> Decimal:
        '20.10'

        c = Decimal(body).quantize(Decimal('1.00'))
        
        return str(c)

    def str(self):
        return self.body