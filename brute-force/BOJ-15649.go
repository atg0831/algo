package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	sc       *bufio.Scanner
	wr       *bufio.Writer
	n        int
	m        int
	selected []int
	used     []bool
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)

	// sc.Split(bufio.ScanWords)
}

func main() {
	defer wr.Flush()

	sc.Scan()
	s := strings.Fields(sc.Text())
	n, _ = strconv.Atoi(s[0])
	m, _ = strconv.Atoi(s[1])

	selected = make([]int, m)
	used = make([]bool, n+1)

	recur(0)
}

func recur(k int) {
	if k == m {
		for _, s := range selected {
			fmt.Fprintf(wr, "%d ", s)
		}
		fmt.Fprintln(wr)
	} else {
		for i := 1; i <= n; i++ {
			if used[i] == false {
				selected[k] = i
				used[i] = true
				recur(k + 1)
				used[i] = false
			}
		}
	}
}
