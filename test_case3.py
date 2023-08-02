class Test_Credence3:

    def test_mul_009(self):
        a = 3
        b = 7
        mul = a * b
        print("Mul of a and b is :" + str(mul))
        if mul == 21:
            assert True
        else:
            assert False