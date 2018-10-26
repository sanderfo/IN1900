def sum_1k(M):
    s = 0
    for k in range(1,M+1):
        s += 1/k
    return s

def test_sum_1k():
    inp = [1, 2, 3]
    out = [1, 3/2, 11/6]
    for e in zip(inp, out):
        expected = e[1]
        computed = sum_1k(e[0])
        result = (expected == computed)
        assert result, "Feil"

test_sum_1k()
