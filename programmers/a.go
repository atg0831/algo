import(
    "strings"
)
func solution(id_list []string, report []string, k int) []int {
    
    idMap := make(map[string]int)
    for idx, id := range id_list {
        idMap[id] = idx
    }
    
    type fromWithIdx struct {
        from string
        idx int
    }
    
    reportToFrom := make(map[string][]fromWithIdx)
    alreadyCheck := false
    for _, eachReport := range report{
        reportSplit := strings.Split(eachReport, " ")
        for _, v := range reportToFrom[reportSplit[1]]{
            if v.from == reportSplit[0] {
                alreadyCheck = true
                break
            }
        }
        if !alreadyCheck{
            reportToFrom[reportSplit[1]] = append(reportToFrom[reportSplit[1]], fromWithIdx{
                from: reportSplit[0],
                idx: idMap[reportSplit[0]],
            })
        }
        alreadyCheck = false
    }
    
    answer := make([]int, len(id_list))
    for _, froms := range reportToFrom {
        if len(froms) >= k {
            for _, from := range froms {
                answer[from.idx] += 1
            }
        }
    }
    
    return answer
}