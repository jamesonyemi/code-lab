<?php

declare(strict_types=1);

require_once __DIR__.'/linked_list_2.php';

use linked_list_2\Node;
use linked_list_2\SinglyLinkedList;

$list = new SinglyLinkedList();

function printResult(string $label, mixed $value): void
{
    echo $label;
    if ($value instanceof Node) {
        echo "Node(data={$value->data})";
    } elseif (is_bool($value)) {
        echo $value ? 'true' : 'false';
    } elseif ($value === null) {
        echo 'null';
    } else {
        echo (string) $value;
    }
    echo PHP_EOL;
}

$list->insert(10);
$list->insert(20);
$list->insert(30);

echo 'Initial list: '.$list->toVisualString().PHP_EOL;
printResult('Search 20: ', $list->search(20));
printResult('Search 99: ', $list->search(99));

printResult('Remove 20: ', $list->remove(20));
echo 'After removing 20: '.$list->toVisualString().PHP_EOL;

$list->insertAt(15, 1);
echo 'After insertAt(15, 1): '.$list->toVisualString().PHP_EOL;
printResult('Count: ', $list->count());
printResult('Remove 99: ', $list->remove(99));
