/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head)
    {
        ListNode*	first = head;
        ListNode*	second = head;
        if (!first || !second)
            return (false);
        while (true)
        {
            if (second->next != nullptr && second->next->next != nullptr)
            {
                second = second->next->next;
            }
            else
                return (false);
            first = first->next;
            if (first == second)
            {
                break;
            }
        }
        return (true);
    }
};