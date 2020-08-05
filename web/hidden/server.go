package main

import (
	"log"
	"net/http"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "index.html")
}

func main() {
	http.HandleFunc("/", Handler)
	log.Fatal(http.ListenAndServe("0.0.0.0:13578", nil))
}
