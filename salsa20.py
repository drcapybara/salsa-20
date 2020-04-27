# salsa20 attempt

#global variable for number of rounds
ROUNDS = 20

#rotating function
def ROTL(b, r):

    s = ( ( ( b << r )) | ( b >> ( 32 - r ) ) ) 
    return s


# quarter round function
def QR(a, b, c, d):

    b ^= ROTL(a + d, 7)	
    c ^= ROTL(b + a, 9)	
    d ^= ROTL(c + b, 13)	
    a ^= ROTL(d + c, 18)


def init(nonce, key, counter):

    nonce = [0]*8
    key = [0]*32
    counter = [0]*8

    n = [nonce[4 * i : 4 * i + 4] for i in range(2)]
    k = [(key[4*i:4*i+4]) for i in range(8)]
    b = [(counter[4*i:4*i+4]) for i in range(2)]


    in0 = [16]
    x = [16]
    i = 0

    while i < ROUNDS:
        
        # run quarter round alg on columns here
        QR(x[0], x[4], x[8], x[12]) 
        QR(x[5], x[9], x[13], x[1])
        QR(x[10], x[14], x[2], x[6])
        QR(x[15], x[3], x[7], x[11])

        # run QR alg on rows here
        QR(x[ 0], x[ 1], x[ 2], x[ 3])
        QR(x[ 5], x[ 6], x[ 7], x[ 4])
        QR(x[10], x[11], x[ 8], x[ 9])
        QR(x[15], x[12], x[13], x[14])