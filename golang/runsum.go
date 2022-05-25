package main

import (
    "fmt"
)

func runningSum(nums []int) []int {
    fmt.Println(nums)
    sum := make([]int, len(nums))
    for i := 0; i <= len(nums)-1; i++ {
        if i == 0 {
            sum[i] = nums[i]
        } else {
            sum[i] = sum[i-1] + nums[i]
        }
    }
    return sum
}

func main() {
    var nums = []int{3,1,2,10, 1}
    x := runningSum(nums)
    fmt.Println(x)
}
