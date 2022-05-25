package main

import (
    "fmt"
)
// Worst way of doing this... But fck it
func searchMatrix(matrix [][]int, target int) bool {
    var ret bool
    fmt.Println(matrix)
    for i:=0; i<=len(matrix)-1; i++ {
        for j:= 0; j<=len(matrix[i])-1; j++ {
            if matrix[i][j] == target {
                ret = true
            }
        }
    }
    return ret
}

func main() {
    m := [][]int {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}
    fmt.Println(m)
    b := searchMatrix(m, 16)
    fmt.Println(b)
}

