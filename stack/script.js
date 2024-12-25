var stack = (arr, item) => {

    console.info(`Array origin: ${arr}`)

    arr.push(item)

    console.info(`Array with add item: ${arr}`)

    arr.pop()

    console.info(`Array remove item: ${arr}`)

}

var arr = [1,2,3,4]

var item = 5

stack(arr, item)