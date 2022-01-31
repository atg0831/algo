package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	sc *bufio.Scanner
	wr *bufio.Writer
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
	sc.Split(bufio.ScanWords)
}

func main() {
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	A := make([]struct {
		value int
		idx   int
	}, n)

	B := make([]struct {
		value int
		idx   int
	}, n)

	for i := 0; i < n; i++ {
		sc.Scan()
		A[i].value, _ = strconv.Atoi(sc.Text())
		A[i].idx = i
	}

	copy(B, A)

	// stable sorting -> sort.Stable 가능
	// 1, 2(1), 2(2), 3, 4, ...
	sort.Slice(B, func(i, j int) bool {
		if B[i].value == B[j].value {
			return B[i].idx < B[j].idx
		}
		return B[i].value < B[j].value
	})

	answer := make([]int, n)

	for i := 0; i < n; i++ {
		answer[B[i].idx] = i
	}

	for _, ans := range answer {
		fmt.Printf("%d ", ans)
	}
}
