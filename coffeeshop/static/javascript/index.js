/**
 * Created by Ritesh on 7/28/2018.
 */
var orders = [];
function itemAdded(itemName,size) {
    console.log(itemName);
    var article = document.getElementById(itemName+'-'+size)
    article.value = parseInt(article.value) + 1;
    console.log(article.dataset.drinkType, itemName, article.value, size);
    var existItem = orders.find(function (ele) {
        if(ele.name === itemName && ele.size === size){
            ele.value = article.value
            return ele
        }
    })
    if(!existItem){
        orders.push({type: article.dataset.drinkType, name: itemName, value: article.value, size: size})
    }
    console.log(orders)
}

function itemSubtract(itemName,size) {
    var article = document.getElementById(itemName+'-'+size)
    if(parseInt(article.value) !== 0) {
        article.value = parseInt(article.value) - 1;
        orders.find(function (ele) {
            if(ele.name === itemName && ele.size === size) {
                ele.value = article.value
                if(parseInt(ele.value) === 0){
                    orders = orders.filter(function (ele) {
                        return (parseInt(ele.value) != 0)
                    });
                }
            }
        })
    }
    console.log(orders)
}

function orderDetail() {
    console.log('order detail is progress', orders)
}