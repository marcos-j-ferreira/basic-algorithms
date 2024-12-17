
var arr = [1,4,5,6,7,8]

var ord = arr.sort()

var index = 0;


var number = 8;

var meio= 0 ;

var size = arr.length - 1

while (index <= size){

    meio = (index + size) / 2

    if (arr[meio] == number){
        return console.info(meio)
    }else if(number < arr[meio]){
        size = meio - 1
    }else{
        index = meio + 1
    }

}

console.info(ord)


