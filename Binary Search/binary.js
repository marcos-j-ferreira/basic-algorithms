var search = (arr, target) => {
    

    index = 0;
    end = arr.length - 1;

    while( index <= end){

        middle = Math.floor(( index + end) / 2);

        if(arr[middle] == target){
            return middle
        }else if(arr[middle] < target){
            index = middle + 1
        }else{
            end = middle - 1
        }
    }return -1
}

var arr = [1,2,3,4,5];

var target = 5;

var result = search(arr, target);

if(result == -1){
    console.log("Númeor não encontrado")
}else{
    console.log(`Númeor encontrado no índice ${result}`)
}