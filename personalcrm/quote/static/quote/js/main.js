document.addEventListener('DOMContentLoaded', function () {
  let new_quote_button = $('#new_quote_button');

  if (new_quote_button) {
    new_quote_button.click(() => (location.href = 'create-quote'));
  }

  $('.datepicker').datepicker();

  rowFieldsFunction();

  $('#new-item').click(() => addNewLine());

  rowNumberUpdate();

  quote_row = $('#initial-row').prop('outerHTML');

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

function rowFieldsFunction() {
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
    rowNumberUpdate();
  });

  $('.hidden-field').change((e) => {
    let tr = e.target.closest('tr');
    hideRow(tr);
  });
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

function hideRow(tr) {
  if ($(tr).find('.hidden-field').val() == 'True') {
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

  let line = quote_row;

  $('tbody').append(line);

  rowNumberUpdate();

  rowFieldsFunction();
}

function rowNumberUpdate() {
  rows = $('.row-number');

  for (let i = 0; i < rows.length; i++) {
    $(rows[i]).html(i + 1);
  }
}
