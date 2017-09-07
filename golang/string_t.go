package main

import (
    "fmt"
    "strings"
    "strconv"
)

func main() {
    t0 := "\u6B22\u8FCE\u6765\u5230" // t0内容：欢迎来到
    t1 := "\u5B9E\u9A8C\u697C"       // t1内容：实验楼
    t2 := t0 + t1
    for index, char := range t2 {
        fmt.Printf("%-2d    %U      '%c'    %X      %d\n",
            index, char, char, []byte(string(char)), len([]byte(string(char))))
    }
    fmt.Printf("length of t0: %d, t1: %d, t2: %d\n", len(t0), len(t1), len(t2))
    fmt.Printf("content of t2[0:2] is: %X\n", t2[0:2])

    var str string = "go_lang"
    fmt.Printf("T/F? Does the string \"%s\" have prefix \"%s\"? ", str, "go")
    fmt.Printf("%t\n", strings.HasPrefix(str, "go"))
    fmt.Printf("T/F? Does the string \"%s\" contains \"%s\"? ", str, "-")
    fmt.Printf("%t\n", strings.Contains(str, "-"))
    str_new := strings.Replace(str, "go", "python", 1)
    fmt.Printf("Origin string: \"%s\", after replace: \"%s\"\n", str, str_new)
    fmt.Printf("Number of 'n' in \"%s\" is: %d\n", str_new, strings.Count(str_new, "n"))

    var ori string = "123456"
    var i int
    var s string

    fmt.Printf("The size of ints is: %d\n", strconv.IntSize)

    i, _ = strconv.Atoi(ori)
    fmt.Printf("The integer is: %d\n", i)
    i = i + 5
    s = strconv.Itoa(i)
    fmt.Printf("The new string is: %s\n", s)
}
