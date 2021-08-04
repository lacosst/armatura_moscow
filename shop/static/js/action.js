// Удаление сообщения
const deleteNode = document.querySelector("button.btn-primary");
deleteNode.addEventListener("click", () => {
  const divDelete = document.querySelector("div.alert");
  if (divDelete) {
    divDelete.innerHTML = "";
    divDelete.remove();
  }
});
const bodyCheck = document.body;
bodyCheck.addEventListener("click", () => {
  const delMess = document.querySelector("div.alert");
  if (delMess) {
    // console.log(delMess);
    delMess.innerHTML = "";
    delMess.remove();
  }
});

// const cartPlus = document.querySelector('button.cart_plus')
// cartPlus.addEventListener('click', ()=>{

//     console.log(cartPlus)
// })

function workMessenger(count_item_cart, msg, total_pice_cart, quantity) {
    
    //alert("Спасибо, что обратились к нам ");
    const shopping = (' ' + count_item_cart + ' позиции на сумму ' + total_pice_cart + ' руб.')
    const iClass = document.getElementById('subheader').querySelector('div.cart')
    //Удаление элемента
    while (iClass.firstChild) {
        iClass.removeChild(iClass.lastChild);
    }
    
    //Добавление элемента
    const textPosition = '<i class="bi bi-cart-check"></i><a class="text-white text-decoration-none" href="/cart/">' + shopping + '</a>'
    iClass.insertAdjacentHTML('beforeend', textPosition)
    
    //Создание сообщения
    let divCont = document.createElement('div')
    divCont.className = 'alert alert-success mx-auto text-center '
    divCont.innerHTML = '<i class="bi bi-check-circle-fill"> </i>' + msg
    document.querySelector('nav.navbar').after(divCont)
}