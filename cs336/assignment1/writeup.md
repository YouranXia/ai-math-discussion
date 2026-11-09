
### 2.1 unicode
- (a) Null.
- (b) It indicates that the character is a string. 
- (c) It turns out to be interpreted as the ascii number of the character.

### 2.2
- (a) It can save the amount of space it needs to store the same things. 
- (b) Maybe there is a character that needs to be transfered to more than onr byte, like '你'. (Rmk: the code refers to transfering to one byte at a time, which isn't always true.) 
- (c) **80 80** (Rmk: UTF-8 uses "110***** 10******" to encode a character, but it is only for characters like 'a' or 'b'. However, 80 is a number whose binary representation is "10000000". It doesn't fit into the UTF-8 format.)

