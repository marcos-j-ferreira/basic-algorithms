var busca_linear_invertida = (arr, number) => {

    var size = arr.length

    for(var i = size; i > 0; i--){
        if( number == arr[i]){
            return true
        }
    }

    return false


}


var arr = [1,2,3,4,5];

var number = 6;

var result = busca_linear_invertida(arr, number);

console.info(`\n  ${result} \n`)