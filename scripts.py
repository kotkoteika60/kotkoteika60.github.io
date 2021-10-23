import base64

edc = lambda bs: "0" if len(list(filter(lambda x: x == "1", list(bs)))) % 2 == 0 else "1"

def bit_decode(bs): # 0101010010100...
    bs = bs.replace(" ", "")
    s = b""
    for i in range(0, len(bs), 8):
        s += bytes([int(bs[i:i+8], 2)])
    return s.decode("cp1251")

def cp1251decode(bs): # 23 53 65...
    s = b""
    for i in bs.strip().split():
        s += bytes([int(i)])
    return s.decode("cp1251")

def snickers(bs):
    return bs.replace(" ", "")[::-1]

def hamming_decode(bs):
    result = ""
    for i in bs.strip().split():
        magic = ""
        _1bit = i[::2]
        _2bit = i[1:3] + i[5:7] + i[9:11] + i[13:]
        _4bit = i[3:7] + i[11:]
        _8bit = i[7:]
        magic += "1" if edc(_8bit[1:]) != i[7] else "0"
        magic += "1" if edc(_4bit[1:]) != i[3] else "0"
        magic += "1" if edc(_2bit[1:]) != i[1] else "0"
        magic += "1" if edc(_1bit[1:]) != i[0] else "0"
        magic = int(magic, 2)
        if magic:
            print(f"(лог) ошибка в бите {magic}")
            _r = list(i)
            _r[magic-1] = "1" if _r[magic-1] == "0" else "0"
            _r = "".join(_r)
            res = _r[2] + _r[4:7] + _r[8:]
            result+=res
        else:
            res = i[2] + i[4:7] + i[8:]
            result+=res
    return result + ("0" * (len(result) % 8))

def rle_decode(bs):
    d = ["1", "010", "011", "00100", "00101", "00110", "00111", "0001000", "0001001"]
    result = ""
    gb, data = bs[0], bs[1:]
    temp = ""
    for i in data:
        temp+=i
        if temp in d:
            n = d.index(temp) + 1
            result += gb * n
            if gb == "1": gb = "0"
            elif gb == "0": gb = "1"
            temp = ""
    return result