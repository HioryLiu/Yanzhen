package main

import  (
	"fmt"
	"math"
	"errors"
	)

func main() {
	const LENGTH int = 10
	const WIDTH int = 5
	var area int 
	const a1, b1, c1 =1, false, "str"

	area = LENGTH * WIDTH
	fmt.Printf("area is : %d", area)

/*	const (
		a= iota
		b
		c
		d="haha"
		e
		f =100
		g
		h = iota
		i
	)

	fmt.Println(a, b, c, d, e, f, g, h, i)*/

	for x := 0; x<10; x++ {
		fmt.Printf("x is %d\n", x)
	}
	nums := [6]int{1, 2, 3, 5}
	for i,v := range nums {
		fmt.Printf("%dth = %d\n", i, v)
	}

	for i := 0; i < 10; i++ {
		for j :=0; j <10; j++{
			if j%2==0 {
				continue
			}
			fmt.Println(i,j)
		}

		fmt.Printf("this is")
	}

	for i := 0; i < 10; i++ {
		if i==5 {
			goto PRINT
		}
	}

	PRINT: fmt.Printf("this is from goto\n")

	m1, m2 := swap("dong", "liu")
	fmt.Println(m1, m2)

	n1, n2 := 100, 200
	swapInt(&n1, &n2)
	fmt.Println(n1, n2)

	getSquareRoot := func(x float64) float64 {
		return math.Sqrt(x)
	}
	fmt.Println(getSquareRoot(9))//go closure

	nextNumber := getSequence()
	fmt.Println(nextNumber())
   	fmt.Println(nextNumber())
   	fmt.Println(nextNumber())

   	var circle Circle
   	circle.radius = 10.00
   	fmt.Println(circle.getArea())

   	fmt.Println(out)

   	arr := []int{10, 100, 200}
   	const MAX int = 3
   	var i int
   	var ptr [MAX]*int

   	for i = 0; i< MAX; i++ {
   		ptr[i] = &arr[i]
   	}

   	for i = 0; i < MAX; i++ {
   		fmt.Printf("a[%d] = %d\n", i,*ptr[i] )
   	}

   	var zhint int = 3000
   	var ptr1 *int
   	var pptr1 **int

   	ptr1 = &zhint
   	pptr1 = &ptr1

   	fmt.Println(zhint, ptr1, pptr1)

   	//slice
   	var numbers = make([]int, 3, 5)
   	fmt.Println(len(numbers), cap(numbers), numbers)

   	// map & range
   	kvs := map[string]string{"a": "apple", "b": "banana"}
   	for k, v := range kvs {
   		fmt.Printf("%s -> %s", k, v)
   	}

   	for i, c := range "golang" {
   		fmt.Println(i, c)
   	}

   	v, ok := kvs["a"]
   	if (ok) {
   		fmt.Println(v)
   	}
   	delete(kvs, "a")
   	fmt.Println(kvs)

   	// error

   	result, err := Sqrt(-1)
   	if err != nil {
   		fmt.Println(err, result)
   	}



}

func Sqrt(f float64) (float64, error) {
	if f <0 {
		return 0, errors.New("math: cannot be negative number")
	}
	return 0, errors.New("math: cannot be negative number")
}

type error interface{
	Error() string
}

type Phone interface {
	call()
}

type Books struct {
	title string
	author string
	subject string
	book_id int
}

func swap(x, y string) (string, string) {
	return y, x
}

func swapInt(x *int, y *int) {
	tmp := *x
	*x = *y
	*y = tmp
}

func getSequence() func() int {
	i := 0
	return func() int {
		i+=1
		return i
	}
}

type Circle struct {
   	radius float64
}

func (c Circle) getArea() float64 {
	return 3.14 * c.radius * c.radius
}

var out int