import bond_func

def test_Bond():
    assert round(bond_func.getBondDuration(0.03,0.04,1,10),2) == 8.51
    

