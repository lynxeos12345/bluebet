#-*—coding:utf8-*-

import base58

cardPool52 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
            39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]

def shuffle(sig):
    decode = base58.b58decode(sig)

    cards = [0 for i in range(52)]
    dealCnt = 0
    decodeIndex = 0
    ascNum = ord(decode[decodeIndex])
    while(dealCnt < 52):
        if(dealCnt >= 52):
            break
        index = int(ascNum) % (dealCnt + 1)
        for i in range(dealCnt, index, -1):
            cards[i] = cards[i - 1]
        cards[index] = cardPool52[dealCnt]
        dealCnt += 1
        decodeIndex += 1
        if decodeIndex == len(decode):
           decodeIndex = 0
        ascNum = ord(decode[decodeIndex])
    return cards

if __name__ == '__main__':
    '''
    signature public key:EOS6QoktH8i3ufB1Rp9UwytVdkTxFwd4tZMK6bBbNKKWyB2tX1iH8
    signature content: server_seed, player_seed, block_hash
    Black Jack:server_seed + player_seed
    Three Cards:server_seed + player_seed
    Caribbean:server_seed + player_seed
    Baccarat:server_seed + block_hash
    Bulls:server_seed + block_hash
    '''
    sig = "KwKar2B3NZWPebRtwHaCwbfvoEc3V33RMKzNhJtE1YdcNQqghefFjLXid86AFryd3qihqaJ8tGx5dBLg4qJp6bbN7doivw"

    cards = shuffle(sig)
    print "signature:", sig
    print "shuffled cards:"
    print cards


    print "================================================================\n\
number to card:\n\
        A  2  3  4  5  6  7  8  9  10  J  Q  K\n\n\
diamond 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,\n\
heart   13,14,15,16,17,18,19,20,21,22,23,24,25,\n\
spade   26,27,28,29,30,31,32,33,34,35,36,37,38,\n\
club    39,40,41,42,43,44,45,46,47,48,49,50,51,"
    

    



