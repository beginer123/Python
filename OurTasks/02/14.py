integer = int (input ())
_3 = ((integer & (1 <<  3)) // (1 <<  3));
_4 = ((integer & (1 <<  4)) // (1 <<  4));
_5 = ((integer & (1 <<  5)) // (1 <<  5));
_24 = ((integer & (1 << 24)) // (1 << 24));
_25 = ((integer & (1 << 25)) // (1 << 25));
_26 = ((integer & (1 << 26)) // (1 << 26));
integer -=  _3 <<  3;
integer -=  _4 <<  4;
integer -=  _5 <<  5;
integer -= _24 << 24;
integer -= _25 << 25;
integer -= _26 << 26;
integer +=  _3 << 24;
integer +=  _4 << 25;
integer +=  _5 << 26;
integer += _24 <<  3;
integer += _25 <<  4;
integer += _26 <<  5;
print (integer);