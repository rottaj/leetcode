package main

import (
    "fmt"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    x := append(nums1, nums2...)
    sum := 0
    for i:=0; i <= len(x)-1; i++ {
       sum += x[i]
    }
    var med float64
    var sumFloat float64 = float64(sum)
    var lenFloat float64 = float64(len(x))
    med = sumFloat / lenFloat
    return med

}
func main() {
    x1 := [2]int {1,3}
    x2 := [2]int {2,7}
    x := findMedianSortedArrays(x1[:], x2[:])
    fmt.Println(x1,x2, x)
}
