<?php
declare(strict_types=1);
namespace linked_list_2;


use InvalidArgumentException;
use OutOfBoundsException;

class Node
{
    public function __construct(
        public mixed $data,
        public ?Node $next = null,
    ){}
}


class SinglyLinkedList
{
    public function __construct(private ?Node $head = null){}

    public function insert($data): void
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

    public function search(mixed $key): ?Node
    {
        $current = $this->head;

        while ($current) {
            if ($current->data === $key) {
                return $current;
            }
            $current = $current->next;
        }

        return null;
    }

    public function insertAt(mixed $data, int $index): void
    {
        if ($index < 0) {
            // code...
            throw new InvalidArgumentException('index cannot be negative', 1);
        }

        $newNode = new Node($data);

        if ($index === 0) {
            $newNode->next = $this->head;
            $this->head = $newNode;

            return;
        }

        $current = $this->head;
        $position = 0;

        while ($current !== null && $position < $index - 1) {
            $current = $current->next;
            ++$position;
        }

        if ($current === null) {
            throw new OutOfBoundsException('index out of range');
        }

        $newNode->next = $current->next;
        $current->next = $newNode;
    }

    public function remove(mixed $key): ?Node
    {
        $current = $this->head;
        $previous = null;

        while ($current !== null) {
            if ($current->data === $key) {
                if ($previous === null) {
                    $this->head = $current->next;
                } else {
                    $previous->next = $current->next;
                }

                $current->next = null;

                return $current;
            }

            $previous = $current;
            $current = $current->next;
        }

        return null;
    }

    // 1. Add Countable support to know the size in O(N) time
    public function count(): int
    {
        $count = 0;
        $current = $this->head;
        while ($current !== null) {
            ++$count;
            $current = $current->next;
        }

        return $count;
    }

    // 2. Add a display string helper for easy terminal debugging
    public function toVisualString(): string
    {
        $elements = [];
        $current = $this->head;
        while ($current !== null) {
            $elements[] = "[{$current->data}]";
            $current = $current->next;
        }

        return implode(' -> ', $elements) ?: 'Empty List';
    }
}
