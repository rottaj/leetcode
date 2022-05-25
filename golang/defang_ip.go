package main
import (
    "fmt"
    "strings"
)
func defangIPaddr(address string) string {
    a := strings.Split(address, "")
    fmt.Println(a)
    for i :=0; i <= len(a)-1; i++ {
        if a[i] == "." {
            a := a[:i]
            a = append(a, "[.]")
        }
    }
    var x string = strings.Join(a, "")
    return x
}


func main() {
    addr := "192.168.1.10"
    x := defangIPaddr(addr)
    fmt.Println(x)
}
