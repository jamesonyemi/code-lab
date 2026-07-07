package main

import (
    "encoding/json"
    "net/http"
    "log"
    "io/ioutil"
    "fmt"
)

// PaymentRequest represents the incoming request payload
type PaymentRequest struct {
    IDempotencyKey string `json:"idempotency_key"`
    Amount           int    `json:"amount"`                                                                                                                                
}

// Payment represents a payment record
type Payment struct {
    ID     string `json:"id"`
    Amount int    `json:"amount"`
    Status string `json:"status"`
}

// UserStore is the interface we defined earlier
type UserStore interface {
    CreatePayment(req PaymentRequest) (Payment, error)
    GetPayment(id string) (Payment, bool)
}

// InMemoryStore is a simple in-memory implementation of UserStore
type InMemoryStore struct {
    payments map[string]Payment
    keys     map[string]string
}

// NewInMemoryStore initializes the store
func NewInMemoryStore() *InMemoryStore {
    return &InMemoryStore{
        payments: make(map[string]Payment),
        keys:     make(map[string]]string),
    }
}

// CreatePayment stores the payment and ensures idempotency
func (m *InMemoryStore) CreatePayment(req PaymentRequest) (Payment, error) {
    if paymentID, exists := m.keys[req.IDempotencyKey]; exists {
        // If already used, return the existing payment
        return m.payments[paymentID], nil
    }
    // Create a new payment
    payment := Payment{
        ID:     req.IDempotencyKey,
        Amount: req.Amount,
        Status: "SUCCESS",
    }
    m.payments[payment.ID] = payment
    m.keys[req.IDempotencyKey] = payment.ID
    return payment, nil
}

// GetPayment retrieves a payment by ID
func (m *InMemoryStore) GetPayment(id string) (Payment, bool) {
    p, ok := m.payments[id]
    return p, ok
}

// PaymentHandler is the HTTP handler for creating payments
func PaymentHandler(store UserStore) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        // Read request body
        body, err := ioutil.ReadAll(r.Body)
        if err != nil {
            http.Error(w, "Unable to read request", http.StatusBadRequest)
            return
        }
        defer r.Body.Close()

        // Decode JSON
        var req PaymentRequest
        if err := json.Unmarshal(body, &req); err != nil {
            http.Error(w, "Invalid JSON", http.StatusBadRequest)
            return
        }

        // Call the store's CreatePayment method
        payment, err := store.CreatePayment(req)
        if err != nil {
            http.Error(w, "Failed to create payment", http.StatusInternalServerError)
            return
        }

        // Return the payment as JSON
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(payment)
    }
}

func main() {
    store := NewInMemoryStore()

    http.HandleFunc("/payments", PaymentHandler(store))

    fmt.Println("Server running on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}	