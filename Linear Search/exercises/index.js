var busca_linear_invertida = (arr, number) => {

    var size = arr.length

    for(var i = size; i > 0; i--){
        if( number == arr[i]){
            return true
        }
    }

    return false


}

var contagem_ocorrencias = (arr, number) => {

    var r = 0;

    for(var i =0; i < arr.length; i++){

        if(number == arr[i]){
            r++;
        }
    }
    return r;
}

var arr = [1,2,3,4,5,3,1,1];

var number = 1;

var result = contagem_ocorrencias(arr, number);

console.info(`\n  ${result} \n`)