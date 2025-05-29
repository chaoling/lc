#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d): data(d), next(nullptr) {}
};

// Utility: print list
void printList(Node* head) {
    for (auto p = head; p; p = p->next)
        cout << p->data << " ";
    cout << "\n";
}

// Split the list into two halves, return middle node
Node* getMiddle(Node* head) {
    if (!head) return head;
    Node *slow = head, *fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

// Merge two sorted lists
Node* mergeLists(Node* a, Node* b) {
    if (!a) return b;
    if (!b) return a;
    if (a->data < b->data) {
        a->next = mergeLists(a->next, b);
        return a;
    } else {
        b->next = mergeLists(a, b->next);
        return b;
    }
}

// Recursive merge-sort
Node* mergeSort(Node* head) {
    if (!head || !head->next) return head;
    Node* mid = getMiddle(head);
    Node* right = mid->next;
    mid->next = nullptr;
    Node* left_sorted  = mergeSort(head);
    Node* right_sorted = mergeSort(right);
    return mergeLists(left_sorted, right_sorted);
}

int main() {
    // build list: 4→2→1→3
    int vals[] = {4, 2, 1, 3};
    Node* head = new Node(vals[0]);
    Node* p = head;
    for (int i = 1; i < 4; ++i) {
        p->next = new Node(vals[i]);
        p = p->next;
    }

    cout << "Before: ";
    printList(head);

    head = mergeSort(head);

    cout << "After:  ";
    printList(head);
    return 0;
}

//g++ -std=c++11 linked_list_mergesort.cpp -o linked_list_mergesort
//./linked_list_mergesort