<?php

class Solution
{
    /**
     * @return int
     */
    public function __construct(
        public $largest = -1,
        public $sec_largest = -1,
    ) {}

    public function secondHighest($s)
    {
        $split_string = str_split($s);

        foreach ($split_string as $char) {
            if (!ctype_digit($char)) {
                continue;
            }

            $digit = (int) $char;

            if ($digit > $this->largest) {
                $this->sec_largest = $this->largest;
                $this->largest = $digit;
            } elseif ($digit > $this->sec_largest && $digit != $this->largest) {
                $this->sec_largest = $digit;
            }
        }

        return $this->sec_largest;
    }
}
