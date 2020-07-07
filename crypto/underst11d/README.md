# Underst11d

I was against the name "underst11d" for this chall.
I think it should be called "matroska".


**Hint**: Try using what you learned from the `understood` series.



**Obs (ctf crew)**: Give the file `flag.txt` for contestants
**Flag**: `mlh{0h_n0w_1_0h_n0w_1_0h_n0w_1_0h}`

**Solution**: Simply decode the `txt` file multiple times:
1. Bin to ascii => base64 string;
2. Base64 decode => base32;
3. Base32 decode => flag;

