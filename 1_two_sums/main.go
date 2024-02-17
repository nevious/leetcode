/*
 * Just trying to get the traverse_map from mani.py working
*/

package main

import (
	"os"
	"fmt"
	"strconv"
)

/* About 2ms on leetcode */
func twoSum(num []int, target int) []int {
	lookup := make(map[int]int)

	for index, element := range(num){
		search := target - element

		if value, ok := lookup[search] ; ok {
			return []int{value, index}
		}

		lookup[element] = index
	}

	return nil
}


func main() {
	/* go is "simple".. yeah..  */
	args := make([]int, len(os.Args)-2)
	last := os.Args[len(os.Args)-1]

	target, err := strconv.Atoi(last)

	if err != nil {
		fmt.Printf("Crashed figuring out target: %v, %T\n", err, err)
		os.Exit(2)
	}

	for index, item := range os.Args[1:len(os.Args)-1] {
		number, err := strconv.Atoi(item)
		if err != nil {
			fmt.Printf("Crashed figuring out  number element: %v, %T\n", err, err)
		}
		args[index] = number
	}

	fmt.Printf("Numbers value: %v and type %T\n", args, args)
	fmt.Printf("Target value: %v and type %T\n", target, target)

	fmt.Println(twoSum(args, target))
}
