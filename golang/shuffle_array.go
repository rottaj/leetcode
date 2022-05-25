package main

import (
    "fmt"
)

func shufflenums(nums []int, n int) []int {
    //ret := make([]int, len(nums))
    var ret []int
    for i := 0; i<= (len(nums) / 2)-1; i++ {
        var temp [2]int
        temp[0] = nums[i]
        temp[1] = nums[i+4]
        ret = append(ret, temp)
        /*
        ret[i] = nums[i]
        ret[i+1] = nums[i+4]
        fmt.Println(i, ret)
        */
    }
    return ret
}

func main() {
    nums := []int{1,2,3,4,4,3,2,1}
    n := 4
    x := shufflenums(nums, n)
    fmt.Println(x)
}
