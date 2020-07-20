# Sculptures


Larson does a bunch of stuff besides rocking at the CTF team. His last endeavor
was carpentry. He's been doing all sorts of interesting wooden sculptures!
He's now looking into a new technique: wood carving.

In the mean time, I, Gabriel, have also been doing a lot of productive
stuff like [watching low quality minecraft memes on youtube](https://www.youtube.com/watch?v=dgha9S39Y6M).
I was having internet issues so I downloaded the video so I could keep watching when internet was down. Here take a look!

I don't know why I keep telling you all this nonsense, here are some random numbers:

`bs=1`
`skip=13306`
`count=41`


**Obs (ctf crew)**: Give the `mining-away.mp4` file to contestants

**Flag**: `mlh{c4rving_4w4y_i_d0nt_kn0w}`

**Solution**:
1. `dd if=./mining-away.mp4 of=./out-flag bs=1 skip=13306 count=41`
2. `base64 -d out-flag`

