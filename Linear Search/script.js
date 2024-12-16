var arr = [1,2,3,4,5];

var number = 4;

function Linear(arr, number) {

    for(var i =0; i < arr.length; i++){
        if(number == arr[i]){
            return true
        }
    }
    return false
}

var result = Linear(arr, number)

console.info(result)
