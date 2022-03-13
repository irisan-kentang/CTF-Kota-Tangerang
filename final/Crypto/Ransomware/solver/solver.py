#!/usr/bin/python3

def xor(s1, s2):
    return bytes(a ^ b for a, b in zip(s1, s2))

def main():
    p1 = open('gambar.jpg', 'rb').read()
    c1 = open('gambar.jpg.menangid', 'rb').read()[9:]
    c2 = open('dokumen rahasia.pdf.menangid', 'rb').read()[9:]

    k = xor(p1[:len(c2)], c1[:len(c2)])
    res = xor(k, c2)
    
    f = open('flag.pdf', 'wb')
    f.write(res)
    f.close()

if __name__ == '__main__':
    main()