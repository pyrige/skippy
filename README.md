# skippy
**skippy** is a 80-bit key, 32-bit block cipher based on Skipjack.
The Python code for the algorithm is a direct translation from C to Python of
[skip32.c by Greg Rose](http://www.qualcomm.com.au/PublicationsDocs/skip32.c).

## Example Usage
```python
>>> import skippy
>>> key = b"s3cr3t_k3y"
>>> cipher = skippy.Skippy(key)
>>> encrypted = cipher.encrypt(42)
>>> encrypted
1139197039
>>> decrypted = cipher.decrypt(encrypted)
>>> decrypted
42
```

## License
**skippy** is free and unencumbered public domain software.
For more information, see http://unlicense.org/ or the accompanying UNLICENSE file.
