package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/gorilla/mux"
)

func main() {
	// Router'ı oluştur
	router := mux.NewRouter()

	// /index için route'ı tanımla
	router.HandleFunc("/index", handleIndex).Methods("GET")

	// Her bir HTTP isteği için goroutine çalıştır

	go makeRequests("http://127.0.0.1")
	go makeRequests("http://127.0.0.1/todo")

	// HTTP sunucusunu başlat
	log.Fatal(http.ListenAndServe(":7880", router))
}

func makeRequests(url string) {

	for i := 0; i < 4000; i++ {
		rand.Seed(time.Now().UnixNano())

		// 1 ile 100 arasında rastgele bir tam sayı üret
		randomNumber := rand.Intn(10) + 1

		fmt.Println("Random Number:", randomNumber)
		request_time := time.Duration(randomNumber) * time.Second
		client := &http.Client{
			Timeout: request_time,
		}

		startTime := time.Now()

		req, err := http.NewRequest("GET", url, nil)
		if err != nil {
			log.Println("Hata:", err)
			continue
		}

		response, err := client.Do(req)
		if err != nil {
			log.Println("Hata:", err)
			continue
		}

		defer response.Body.Close()

		duration := time.Since(startTime)
		fmt.Printf("Durum: %s, Süre: %s\n", response.Status, duration)

		time.Sleep(1 * time.Second)
	}
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Merhaba, Dünya!")
}
