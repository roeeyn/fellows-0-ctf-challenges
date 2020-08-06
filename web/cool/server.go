package main

import (
	"fmt"
	"log"
	"net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	userAgent := r.Header.Get("User-Agent")

	if userAgent == "cool" {
		fmt.Fprintf(w, "mlh{0mg_y0ur_s0000_c00001}")
		return
	}
	fmt.Fprintf(w, "Hey! You're not cool, you're "+userAgent)
}

func main() {
	http.HandleFunc("/", Handler)
	log.Fatal(http.ListenAndServe("0.0.0.0:11881", nil))
}
