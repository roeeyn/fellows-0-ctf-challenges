# Pics on a Pipe

Back in the old days of no internet and no computers people thought
they would never be able to put a picture on a pipe and send it to
others.

Today that's kinda possible though.


**Hint**: Install Wireshark and look at the `pcap` file

**Obs (ctf crew)**: Give the `pics-on-a-pipe.pcap` file to contestants

**Flag**: `mlh{p1p3z_4r3_p0w3rful_4s_h3ck}`

**Solution**:
1. Open `pics-on-a-pipe.pcap` on Wireshark
2. File > Export Objects > HTTP > save to a file
3. Open the saved file (outputs the image with the flag)

