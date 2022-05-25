package main

import (
    "fmt"
    "strconv"
    "strings"
)

func reverse(x int) int {
    r := strconv.Itoa(x)
    a := strings.Split(r, "")
    var a1 []string
    for i:=len(a)-1; i>= 0; i-- {
        a1 = append(a1, a[i])
    }
    j := strings.Join(a1, "")
    ret, err := strconv.Atoi(j)
    if err != nil{
        a1 = a1[:len(a1)-1]
        j := strings.Join(a1, "")
        ret, err = strconv.Atoi(j)
        ret = ret * -1
    }
    return ret
}

func main() {
    //x1 := 321324234
    x1 := -321324234
    x := reverse(x1)
    fmt.Println(x)
}
