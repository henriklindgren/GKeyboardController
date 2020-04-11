VENDOR_ID = 0x0c45
PRODUCT_ID = 0x652f

INTERFACE = 1
SETTING = 0
IN_ENDPOINT_NUM = 0
OUT_ENDPOINT_NUM = 1

TOTAL_KEY_COUNT = 104
SECTION_0_KEY_COUNT = 77
SECTION_1_KEY_COUNT = 27

# Commands for each of the modes defined in the official software.
MODE_COMMANDS = {
    'wave1':            b'\x04\x08\x00\x06\x01\x00\x00\x00\x01',
    'wave2':            b'\x04\x09\x00\x06\x01\x00\x00\x00\x02',
    'spiralingwave':    b'\x04\x0a\x00\x06\x01\x00\x00\x00\x03',
    'acid':             b'\x04\x0b\x00\x06\x01\x00\x00\x00\x04',
    'breathing':        b'\x04\x0c\x00\x06\x01\x00\x00\x00\x05',
    'normallyon':       b'\x04\x0d\x00\x06\x01\x00\x00\x00\x06',
    'ripplegraff':      b'\x04\x0f\x00\x06\x01\x00\x00\x00\x08',
    'custom':           b'\x04\x1b\x00\x06\x01\x00\x00\x00\x14'
}

# Commands for the 5 brightness levels.
BRIGHTNESS_COMMANDS = [
    b'\x04\x08\x00\x06\x01\x01\x00\x00\x00',
    b'\x04\x09\x00\x06\x01\x01\x00\x00\x01',
    b'\x04\x0a\x00\x06\x01\x01\x00\x00\x02',
    b'\x04\x0b\x00\x06\x01\x01\x00\x00\x03',
    b'\x04\x0c\x00\x06\x01\x01\x00\x00\x04'
]

# 53 zero bits to add to the 11 useful bits.
ZEROES = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Yes, I hate this too. But I don't have a good way of generating these, as it's not as straightforwards as adding 3 every time; there are strange gaps of numbers every now and again.
KEYS = [
    3,
    6,
    9,
    12,
    15,
    18,
    21,
    24,
    27,
    30,
    33,
    36,
    39,
    54,
    57,
    60,
    63,
    66,
    69,
    72,
    75,
    78,
    81,
    84,
    87,
    90,
    93,
    96,
    99,
    105,
    108,
    111,
    114,
    117,
    120,
    123,
    126,
    129,
    132,
    135,
    138,
    141,
    144,
    147,
    150,
    156,
    159,
    162,
    165,
    168,
    171,
    174,
    177,
    180,
    183,
    186,
    189,
    192,
    195,
    198,
    201,
    207,
    210,
    213,
    216,
    219,
    222,
    225,
    228,
    231,
    234,
    237,
    240,
    243,
    246,
    249,
    252,
    2,
    5,
    8,
    11,
    14,
    17,
    20,
    23,
    26,
    29,
    32,
    35,
    38,
    41,
    44,
    47,
    62,
    65,
    68,
    74,
    77,
    80,
    83,
    86,
    89,
    92,
    95
]

# KEYS = {
#     1,      3,
#     2,      6,
#     3,      9,
#     4,      12,
#     5,      15,
#     6,      18,
#     7,      21,
#     8,      24,
#     9,      27,
#     10,     30,
#     11,     33,
#     12,     36,
#     13,     39,
#     14,     54,
#     15,     57,
#     16,     60,
#     17,     63,
#     18,     66,
#     19,     69,
#     20,     72,
#     21,     75,
#     22,     78,
#     23,     81,
#     24,     84,
#     25,     87,
#     26,     90,
#     27,     93,
#     28,     96,
#     29,     99,
#     30,     105,
#     31,     108,
#     32,     111,
#     33,     114,
#     34,     117,
#     35,     120,
#     36,     123,
#     37,     126,
#     38,     129,
#     39,     132,
#     40,     135,
#     41,     138,
#     42,     141,
#     43,     144,
#     44,     147,
#     45,     150,
#     46,     156,
#     47,     159,
#     48,     162,
#     49,     165,
#     50,     168,
#     51,     171,
#     52,     174,
#     53,     177,
#     54,     180,
#     55,     183,
#     56,     186,
#     57,     189,
#     58,     192,
#     59,     195,
#     60,     198,
#     61,     201,
#     62,     207,
#     63,     210,
#     64,     213,
#     65,     216,
#     66,     219,
#     67,     222,
#     68,     225,
#     69,     228,
#     70,     231,
#     71,     234,
#     72,     237,
#     73,     240,
#     74,     243,
#     75,     246,
#     76,     249,
#     77,     252,
#     78,     2,
#     79,     5,
#     80,     8,
#     81,     11,
#     82,     14,
#     83,     17,
#     84,     20,
#     85,     23,
#     86,     26,
#     87,     29,
#     88,     32,
#     89,     35,
#     90,     38,
#     91,     41,
#     92,     44,
#     93,     47,
#     94,     62,
#     95,     65,
#     96,     68,
#     97,     74,
#     98,     77,
#     99,     80,
#     100,    83,
#     101,    86,
#     102,    89,
#     103,    92,
#     104,    95
# }