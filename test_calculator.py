import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_sub(self):
        assert 5 == calculator.sub(8, 3)

    def test_mult(self):
        assert 5 == calculator.mult(2, 2.5)

    def test_div(self):
        assert 5 == calculator.div(15, 3)

