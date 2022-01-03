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
	selected = make([]int, 0)
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
	sc.Split(bufio.ScanWords)
}

func main() {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	sc.Scan()
	m, _ := strconv.Atoi(sc.Text())

	recur(0, n, m)
	wr.Flush()
}

func recur(k, n, m int) {
	if k == m {
		for _, element := range selected {
			fmt.Fprintf(wr, "%d ", element)
		}
		fmt.Fprintln(wr)
	} else {
		for i := 1; i <= n; i++ {
			selected = append(selected, i)
			recur(k+1, n, m)
			selected = append(selected[:k], selected[k+1:]...)
		}
	}
}
