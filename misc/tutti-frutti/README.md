# Tutti Frutti

I love all the flavors!

1. Web (beep, boop, what does a `robot.txt` has to do with this?)
2. Crypto (lots of numbers heh? 32, 64, ...)
3. Pwning (well, time to go get my corona vaccine injection)

`http://fellowship-ctf.tech:7331`

**Obs (ctf crew)**: Run the web server with `go run server.go`

**Flag**: `mlh{4ll_th3_fl4v0rs_y0u_w4nt}`

**Solution**:

1. Download the file `http://fellowship-ctf.tech:7331/robots.txt`
2. Decode the contents of `robots.txt`: `base64 -d robots.txt > out`
3. Get the strings on the `out` binary: `strings out | grep mlh`
