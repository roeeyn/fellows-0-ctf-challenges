# I hate stego

Steganography, from the greek Steganographiks is the art of making
boring and guessy CTF challs. Hence, this is not a steganography (or "stego")
challenge.

"Well then what the heck kind of non-stego chall is this that has a PNG file?"

If you're asking youself that you're probably missing out on the magic of
messing around with files.


**Obs (ctf crew)**: Give the `i-hate-stego.png` file to contestants

**Flag**: `mlh{i_t0ld_u_it_w4s_n0t_st3go}`

**Solution**:
1. `strings i-hate-stego.png` gives a hint of what you need to do
2. Remove the first four lines of the `i-hate-stego.png` file
3. Open the actual image

