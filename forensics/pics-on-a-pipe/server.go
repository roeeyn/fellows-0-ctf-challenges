package main

import (
	"net/http"
)

func rootHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "pipez.png")
}

func main() {
	http.HandleFunc("/", rootHandler)
	http.ListenAndServe("0.0.0.0:8020", nil)
}
