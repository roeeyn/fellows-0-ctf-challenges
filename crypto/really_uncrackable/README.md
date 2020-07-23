# the_most_uncrackable_crypto_ever_now_with_bug_fixes

Gabriel learned his lesson and is now using his only his one
completely secret key, but he forgot to encrypt his first
message to Larson. He then resent the same message encrypted.
Unfortunately, the message he sent unencrypted wasn't the flag.

`Ogc9EgwMMC0rZD86TQAHGGsmEy45KzgYUhA8XAsSPDogHnUneA==            ("this_is_n0t_4_fl4g_but_y0ur3_so_cl0s3")`


`IwM8GmMLcC0xZSZWJi9VECwePyR8KgsFPQt+GwsDYDo2AXYwFAhJLVIrKyl4IhNvCQJRGA==`


**Obs (ctf crew)**: Give the file `really_uncrackable.py` to contestants
**Flag**: `mlh{0n3_t1m3_p4ds_sh0uld_n0t_b3_us3d_m0r3_th4n_0nc3}`

**Solution**:
1. Bruteforce each character of the key given known ciphertext and correspondent plaintext `python3 solution.py <CIPHERTEXT> <PLAINTEXT>`
2. Remove cycled characters from key (in `NoTaSeCrETKey_at_ALLL_gabeNoTaSeCrETK` the beginning of the string `NoTaSeCrETK` repeats): `NoTaSeCrETKey_at_ALLL_gabe`
3. Put found key in a file named `mykey.txt`
4. Run `myreally.py` passing the ciphertext of the flag

