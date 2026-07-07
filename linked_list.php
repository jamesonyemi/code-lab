<?php

class Node
{
    public function __construct(
        public mixed $data,
        public ?Node $next = null
    ) {}

}

class SinglyLinkedList
{
    public function __construct(private ?Node $head = null) {}

    public function insert(mixed $data): void
    {
        $newNode = new Node($data);

        if ($this->head === null) {
            $this->head = $newNode;
            return;
        }

        $current = $this->head;

        while ($current->next !== null) {
            $current = $current->next;
        }
        $current->next = $newNode;
    }
}
