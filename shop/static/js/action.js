// Удаление сообщения
const deleteNode = document.querySelectorAll('button.btn-primary');
deleteNode.forEach((btnDel)=>{

  btnDel.addEventListener("click", () => {
    const divDelete = document.querySelector("div.alert-success");
    if(divDelete){
      while(divDelete.firstChild){
        divDelete.removeChild(divDelete.lastChild)
        divDelete.remove()
      }
    }
    })
});

const bodyCheck = document.body;
bodyCheck.addEventListener("click", () => {
  const delMess = document.querySelector("div.alert-success");
  if (delMess) {
    // console.log(delMess);
    while(delMess.firstChild){
      delMess.removeChild(delMess.lastChild)
      delMess.remove()
    }
  }
});

function workMessenger(count_item_cart, msg, total_pice_cart, quantity) {
  const shopping =
    " " + count_item_cart + " позиции на сумму " + total_pice_cart + " руб.";
  const iClass = document.getElementById("subheader").querySelector("div.cart");
  // Удаление элемента
  while (iClass.firstChild) {
    iClass.removeChild(iClass.firstChild);
  }

  //Добавление элемента
  const textPosition =
    '<i class="bi bi-cart-check"></i><a class="text-white text-decoration-none" href="/cart/">' +
    shopping +
    "</a>";
  iClass.insertAdjacentHTML("beforeend", textPosition);

  //Создание сообщения
  let divCont = document.createElement("div");  
    divCont.className = 'alert alert-success buy-message mx-auto text-center';
    divCont.innerHTML = '<i class="bi bi-check-circle-fill"> </i>' + msg;
    document.querySelector("nav.navbar").after(divCont);  
}

// При нажатии на кнопки
const btns = document.querySelectorAll('.input-group-text');
btns.forEach((btn) => {
  btn.addEventListener('click', function () {
    const direction = this.dataset.direction;
    const inp = this.parentElement.querySelector('.in');
    const currentValue = Number(inp.value);
    const whoParent = inp.parentNode.parentNode.parentNode.parentNode;
    // let currentPrice = whoParent.childNodes[5].innerHTML;
    let currentPrice = whoParent.childNodes[5].querySelector('.items').innerHTML;
    const whoChildTotal = whoParent.childNodes[7].querySelector('.items');
    let whoChildNumber = Number(currentPrice.split(",").join("."));
    let newValue;
    let newWhoChild;
    if (direction === 'plus') {
      newValue = currentValue + 1;
      newWhoChild = String((newValue * whoChildNumber).toFixed(2)).split('.').join(',');
    } else {
      // newValue = currentValue - 1 > 0 ? currentValue - 1 : 0
      if (currentValue - 1 >= 1) {
        newValue = currentValue - 1;
        newWhoChild = String((newValue * whoChildNumber).toFixed(2)).split('.').join(',');
      } else {
        newValue = 1;
        newWhoChild = currentPrice;
      }
    }
    inp.value = newValue;
    whoChildTotal.innerText = numberWithSpaces(newWhoChild);
  });
});

//При изменении значения в input
const inputValue = document.querySelectorAll('.in')
inputValue.forEach ((inValue) => {
  inValue.addEventListener('input',() => {
    const whoParent = inValue.parentNode.parentNode.parentNode.parentNode;
    const nameGoods = whoParent.childNodes[1].textContent;
    const currentPrice = whoParent.childNodes[5].querySelector('.items').innerHTML;
    const whoChildTotal = whoParent.childNodes[7].querySelector('.items');
    if (+inValue.value <= 0 || undefined){
      correctNum = prompt(`Количество товара ${nameGoods} должно быть больше 0`)
      // console.log('это НОООООООООООООООООООООЛЛЛЛЛЛЛЛЛЛЛЛЛЬ')
      whoChildTotal.innerHTML = currentPrice
      // inValue.value = 1
      inValue.value = correctNum
    }
    let currentValue = (+inValue.value * Number(currentPrice.split(",").join("."))).toFixed(2)
    let changeValue = numberWithSpaces(String(currentValue).split('.').join(','))
    whoChildTotal.innerText = changeValue
    // console.log(inputValue)
  })
})

//Разряды для чисел
function numberWithSpaces(num) {
  let parts = num.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  return parts.join(".");
}
