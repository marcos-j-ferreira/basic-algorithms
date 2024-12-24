var select_sort = (arr) => {
    size = arr.length ;

    for(var i = 0; i < size; i++){
        index = i;

        for(var j = i + 1; j < size; j++){

            if (arr[j] < arr[index]){
                index = j;
            }
        }
        let temp = arr[i];
        arr[i] = arr[index];
        arr[index] = temp;
    }
    console.log(arr)
}
var arr = [1,3,6,7,3,5,0]
select_sort(arr)