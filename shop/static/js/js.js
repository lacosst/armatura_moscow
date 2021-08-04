$(document).ready(function () {

    // отслеживаем событие отправки формы
    $('#add_to_cart').submit(function () {

        // создаем AJAX-вызов
        $.ajax({
            data: $(this).serialize(), // получаем данные формы
            type: $(this).attr('method'), // GET или POST
            url: "{% url 'cart:cart_add' product.id %}",
            // если успешно, то
            success: function (response) {

                console.log(this.data)
                console.log('quantity: ' + response.quantity)
                console.log('msg: ' + response.msg)
                console.log('total_pice_cart: ' + response.total_pice_cart)
                console.log('count_item_cart: ' + response.count_item_cart)
            },
            // если ошибка, то
            error: function (response) {
                // предупредим об ошибке
                alert(response.responseJSON.errors);
                console.log(response.responseJSON.errors)
            }
        });
        return false;
    });
})

