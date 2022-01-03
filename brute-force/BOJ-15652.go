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
	// fmt.Fprintf(wr, "%d %d", n, m)
	recur(0, 1)
}

func recur(k, idx int) {
	if k == m {
		for _, s := range selected {
			fmt.Fprintf(wr, "%d ", s)
		}
		fmt.Fprintln(wr)
	} else {
		for i := idx; i <= n; i++ {
			selected[k] = i
			recur(k+1, i)
		}
	}
}
