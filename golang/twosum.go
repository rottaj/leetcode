package main
import (
    "fmt"
)

func twoSum (nums []int, target int) []int {
    //fmt.Println(nums, target)
    var a [2]int
    counter := 0
    for ; counter <= len(nums)-1; counter++ {
        for counterTwo := len(nums)-1; counterTwo >= 0; counterTwo-- {
            if nums[counterTwo] + nums[counter] == target {
              a = [2]int {counterTwo, counter}
            }
        }
    }
    return a[:]
}

func main() {
    nums := [2]int {3, 3}
    target:= 6
    a := twoSum(nums[:], target)
    return a
}
