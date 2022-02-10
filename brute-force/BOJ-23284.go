package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

type stackType []int

var sc *bufio.Scanner
var wr *bufio.Writer

func init() {
	sc = bufio.NewScanner(os.Stdin)
	wr = bufio.NewWriter(os.Stdout)
	sc.Split(bufio.ScanWords)
}

func main() {
	sc.Scan()
	n, err := strconv.Atoi(sc.Text())
	if err != nil {
		log.Print(err)
		return
	}
	defer wr.Flush()

	// n이 0이면 종료
	if n == 0 {
		return
	}

	// num -> 1~n의 숫자 모음
	// stack -> 숫자들이 적재되는 stack
	// answer -> 가능한 케이스 모음
	num := make([]int, 0, n)
	stack := make(stackType, 0, n)
	answer := make(stackType, 0, n)
	for i := 1; i <= n; i++ {
		num = append(num, i)
	}

	backtracking(n, 0, 0, stack, answer)
	fmt.Fprintln(wr)

}

func (s *stackType) push(element int) {
	*s = append(*s, element)
}

func (s *stackType) pop() int {
	top := (*s)[len(*s)-1]
	// stack에서 빼기
	*s = (*s)[:len(*s)-1]
	return top
}

func backtracking(n, pushCnt, popCnt int, s, answer stackType) {
	// push 횟수랑 pop 횟수가 n이면 한 조합에 대한 탐색은 모두 끝났으므로 출력
	if pushCnt == n && popCnt == n {
		for _, a := range answer {
			fmt.Fprintf(wr, "%d", a)
		}
		fmt.Fprintln(wr)
	}

	// push 횟수가 더 많다는 것은 stack에서 pop을 하는 경우가 가능, stack에서 pop을 하고 재귀 호출
	if pushCnt > popCnt {
		top := s.pop()
		answer.push(top)
		backtracking(n, pushCnt, popCnt+1, s, answer)
		answer.pop()
		s.push(top)
	}

	// stack에 적재하지 않은 숫자가 남아 있으므로 push 후 재귀 호출
	if pushCnt < n {
		s.push(pushCnt + 1)
		backtracking(n, pushCnt+1, popCnt, s, answer)
		s.pop()
	}
}