package main

import (
	"fmt"
	"log"
	"net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	cookie, err := r.Cookie("admin")

	// Set cookie
	if err != nil {
		var c http.Cookie
		c.Name = "admin"
		c.Value = "0"
		http.SetCookie(w, &c)
		return
	}

	if cookie.Value == "1" {
		fmt.Fprintf(w, "mlh{4dm1n_3qu4ls_truuuu}")
		return
	}
	fmt.Fprintf(w, "I'm like santa claus. If you don't have a cookie for me, you better forget your gift.")
}

func main() {
	http.HandleFunc("/", Handler)
	log.Fatal(http.ListenAndServe("0.0.0.0:12334", nil))
}
