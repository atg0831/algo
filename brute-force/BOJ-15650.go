package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc       *bufio.Scanner
	wr       *bufio.Writer
	n, m     int
	selected []int
	used     []bool
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
	sc.Split(bufio.ScanWords)
}

func main() {
	defer wr.Flush()
	sc.Scan()
	n, _ = strconv.Atoi(sc.Text())
	sc.Scan()
	m, _ = strconv.Atoi(sc.Text())

	selected = make([]int, m)
	used = make([]bool, n+1)
	recur(0, 1)
}

func recur(k, start int) {
	if k == m {
		for _, s := range selected {
			fmt.Fprintf(wr, "%d ", s)
		}
		fmt.Fprintln(wr)
	} else {
		for i := start; i <= n; i++ {
			if !used[i] {
				selected[k] = i
				used[i] = true
				recur(k+1, i+1)
				used[i] = false
			}
		}
	}
}
