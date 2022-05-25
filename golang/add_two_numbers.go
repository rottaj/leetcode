package main

import (
    "fmt"
)

type ListNode struct {
    val int
    Next *ListNode
}


func (l *ListNode) traverse(x *[]int) []int{
    if l != nil {
        temp := l.val
        *x = append(*x, temp)
        //fmt.Println(x)
        l.Next.traverse(x)
    }
    return *x
}

func (l *ListNode) insert (node *ListNode) {
    if l.Next != nil {
        l.insert(node)
    }
}



func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var x []int
    var x1 []int
    tree := ListNode{}
    x = l1.traverse(&x)
    x1 = l2.traverse(&x1)
    fmt.Println(x, x1)
    if len(x1) > len(x) {
        for i:= -1; i<= (len(x1)-len(x)); i++ {
           x = append([]int{0}, x...)
        }
    } else if len(x) > len(x1) {
        for i:= -1; i<= (len(x)-len(x1)); i++ {
            x1 = append([]int{0}, x1...)
        }
        fmt.Println(x, x1)
    }
    for i:=len(x)-1; i>=0; i-- {
        fmt.Println(i)
        if i == 0 {
            s := x[i] + x1[i] - 10
            fmt.Println(x[i], " + ", x1[i], "----->", s)
            node := ListNode{s, nil}
            tree.insert(&node)
        } else {
            if x[i] + x1[i] > 9 {
                s := x[i] + x1[i] - 10
                x[i-1] += 1
                fmt.Println(x[i], " + ", x1[i], "----->", s)
                node := ListNode{s, nil}
                tree.insert(&node)
            }
        }

    }
    return &tree
}

func main() {
   //treeOne := ListNode{2, &ListNode{4, &ListNode{3, nil}}}
   //treeTwo := ListNode{5, &ListNode{6, &ListNode{4, nil}}}
   treeOne := ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, nil}}}}}}}
   treeTwo := ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9,nil}}}}
   fmt.Println(treeOne, treeTwo)
   ret := addTwoNumbers(&treeOne, &treeTwo)
   fmt.Println(ret)
}
