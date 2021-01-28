document.addEventListener('DOMContentLoaded', function () {
  let new_quote_button = $('#new_quote_button');

  if (new_quote_button) {
    new_quote_button.click(() => (location.href = 'create-quote'));
  }

  $('.datepicker').datepicker();

  $('.product-options').change((e) => {
    let tr = e.target.closest('tr');
    updateProduct(tr);
  });

  $('.price, .qty, .discount').keyup((e) => {
    let tr = e.target.closest('tr');
    updateAmount(tr);
  });

  $('#shipping-input, #tax-input').keyup(() => {
    updateTotal();
  });

  $('.deleteRowButton').click((e) => {
    let tr = e.target.closest('tr');
    deleteRow(tr);
  });

  $('.hiddenCheck').click((e) => {
    let checkbox = e.target;
    let tr = e.target.closest('tr');
    hideRow(tr, checkbox);
  });

  $('#new-item').click(() => addNewLine());

  console.log('Document loaded!');
});

function updateTotal() {
  let subtotal = 0;
  let amountArray = $('.amount');
  for (let i = 0; i < amountArray.length; i++) {
    subtotal = subtotal + parseFloat(amountArray[i]['innerHTML']);
  }

  let shipping = parseFloat($('#shipping-input').val());
  let tax = parseFloat($('#tax-input').val());
  let tax_amount = (subtotal + shipping) * tax * 0.01;
  let total = subtotal + shipping + tax_amount;

  $('#subtotal-amount').html(subtotal);
  $('#shipping-amount').html(shipping);
  $('#tax-amount').html(tax_amount);
  $('#total-amount').html(total);
}

function updateProduct(tr) {
  let pn = $(tr).find('.product-options').val();

  pn = pn.split(':')[0];

  // TO DO: CATCH ERROR WHEN INPUT DOESNT MATCH SITE
  fetch(`product/${pn}`)
    .then((response) => response.json())
    .then((data) => {
      $(tr).find('.product-title').html(data['title']);
      $(tr).find('.product-brand').html(`Brand: ${data['brand']}`);
      $(tr).find('.product-description').html(data['description']);
    });
}

function updateAmount(tr) {
  let qty = $(tr).find('.qty').val();
  let price = $(tr).find('.price').val();
  let discount = $(tr).find('.discount').val();

  let amount = (qty * price * (100 - discount)) / 100;

  $(tr).find('.amount').html(amount);
  updateTotal();
}

function deleteRow(tr) {
  $(tr).remove();
}

function hideRow(tr, checkbox) {
  if ($(checkbox).is(':checked')) {
    $(tr).css('background-color', 'gainsboro');
  } else {
    $(tr).css('background-color', 'white');
  }
}

function addNewLine() {
  number = parseInt($('th').last().html());
  if (number) {
    number = ++number;
  } else {
    number = 1;
  }

  fetch('request-product-options')
    .then((response) => response.json())
    .then((data) => {
      product_options = data['product_options'];
      let products = '';

      for (key in product_options) {
        products = products.concat(`<option>${product_options[key]}</option>`);
      }

      let line = newLine(products);

      $('tbody').append(line);

      $('.price, .qty, .discount').keyup((event) => {
        let tr = event.target.closest('tr');
        updateAmount(tr);
      });

      $('.deleteRowButton').click((event) => {
        let tr = event.target.closest('tr');
        deleteRow(tr);
      });

      $('.hiddenCheck').click((event) => {
        let checkbox = event.target;
        let tr = event.target.closest('tr');
        hideRow(tr, checkbox);
      });

      $('.product-select').change((e) => {
        let tr = e.target.closest('tr');
        updateProduct(tr);
      });
    });
}

function newLine(products) {
  let line =
    '<tr>' +
    '                        <th scope="row">' +
    number +
    '</th>' +
    '                        <td class="description-column">' +
    '                            <div class="form-group">' +
    '                                <select class="form-select product-select">' +
    '                                <option selected>Select product</option>' +
    `                                ${products}` +
    '                                </select>' +
    '                                <label class="product-title"></label>' +
    '                                <label class="product-brand"></label>' +
    '                                <textarea class="form-control product-description" name="product-description" id="" cols="30" rows="5"></textarea>' +
    '                            </div>' +
    '                        </td>' +
    '                        <td class="qty-column">' +
    '                            <div class="form-group">' +
    '                                <input type="number" class="form-control qty" placeholder="Qty" min="0" step="1">' +
    '                            </div>' +
    '                        </td>' +
    '                        <td class="price-column">' +
    '                            <div class="form-group">' +
    '                                <input type="number" class="form-control price" min="0.01" placeholder="Price">' +
    '                            </div>' +
    '                        </td>' +
    '                        <td class="discount-column">' +
    '                            <div class="form-group">' +
    '                                <input type="number" class="form-control discount" id="discount" placeholder="%" min="0.01" max="99.99">' +
    '                            </div>' +
    '                        </td>' +
    '                        <td class="amount-column">' +
    '                            <div class="amount"></div>' +
    '                        </td>' +
    '                        <td class="hiddenCheck-column">' +
    '                            <div class="form-check">' +
    '                                <input class="form-check-input hiddenCheck" type="checkbox" value="">' +
    '                            </div>' +
    '                        </td>' +
    '                        <td class="deleteRow-column">' +
    '                            <div class="form-check">' +
    '                                <button class="btn btn-danger deleteRowButton" type="button">x</button>' +
    '                            </div>' +
    '                        </td>' +
    '                    </tr>';

  return line;
}
