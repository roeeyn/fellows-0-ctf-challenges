package main

import (
	"fmt"
	"log"
	"net/http"
)

func rootHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi there, I love robots!")
}

func robotsHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "robots.txt")
}

func main() {
	http.HandleFunc("/", rootHandler)
	http.HandleFunc("/robots.txt", robotsHandler)
	log.Fatal(http.ListenAndServe("0.0.0.0:7331", nil))
}
