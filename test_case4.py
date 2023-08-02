class Test_Credence4:

    def test_sub_010(self):
        a = 12
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == 5:
            assert True
        else:
            assert False
