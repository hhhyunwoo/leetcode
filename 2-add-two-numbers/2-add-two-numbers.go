/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import "fmt"

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var l1_len, l2_len int
    
    tmp := l1
    for tmp != nil {
        l1_len++
        tmp = tmp.Next
    }
    tmp = l2
    for tmp != nil {
        l2_len++
        tmp = tmp.Next
    }
    var longList, shortList *ListNode
    if l1_len > l2_len{
        longList = l1
        shortList = l2
    }else{
        longList = l2
        shortList = l1
    }
    
    var ListNodes []ListNode
    var carry,sum int
    for shortList != nil{
        sum = shortList.Val+longList.Val + carry
        carry = sum/10
        newList := ListNode{Val:sum%10}
        ListNodes = append(ListNodes, newList)
        
        shortList = shortList.Next
        longList = longList.Next
    }
    
    for longList != nil{
        sum = longList.Val + carry
        carry = sum/10
        newList := ListNode{Val:sum%10}
        ListNodes = append(ListNodes, newList)
        
        longList = longList.Next
    }
    if carry > 0{
        newList := ListNode{Val:carry}
        ListNodes = append(ListNodes, newList)
    }
    
    for i:=0;i<len(ListNodes)-1;i++{
        ListNodes[i].Next = &ListNodes[i+1]
    }
    
    return &ListNodes[0]
}