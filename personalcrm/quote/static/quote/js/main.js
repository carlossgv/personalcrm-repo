document.addEventListener('DOMContentLoaded', function () {
  if (window.location.pathname.includes('view-quote')) {
    $('nav').remove();
  }

  let new_quote_button = $('#new_quote_button');

  if (new_quote_button) {
    new_quote_button.click(() => (location.href = 'create-quote'));
  }

  $('.datepicker').datepicker().datepicker('setDate', new Date());

  rowFieldsFunction();

  $('#new-item').click(() => addNewLine());

  rowNumberUpdate();

  quote_row = $('#initial-row').prop('outerHTML');

  // Update rows when editing quotes
  $.each($('.product-row'), (index, row) => {
    updateAmount(row);
  });
  console.log('document loaded');
});

// !===========================================================

// TODO Implement accounting.js to format columns
function formatColumns() {}

function updateAmount(tr) {
  let qty;
  let price;
  let discount;

  if (window.location.pathname.includes('view-quote')) {
    qty = $(tr).find('.qty').html();
    price = $(tr).find('.price').html();
    discount = $(tr).find('.discount').html();
  } else {
    qty = $(tr).find('.qty').val();
    price = $(tr).find('.price').val();
    discount = $(tr).find('.discount').val();
  }

  let amount = (qty * price * (100 - discount)) / 100;

  $(tr)
    .find('.amount')
    .html(accounting.formatMoney(amount, { precision: 0 }));
  updateTotal();
}

function updateTotal() {
  let subtotal = 0;
  let amountArray = $('.amount');
  for (let i = 0; i < amountArray.length; i++) {
    subtotal = subtotal + accounting.unformat(amountArray[i]['innerHTML']);
  }

  let tax;

  if (window.location.pathname.includes('view-quote')) {
    tax = accounting.unformat($('#tax-input').html());
  } else {
    tax = parseFloat($('#tax-input').val());
  }

  let tax_amount = subtotal * tax * 0.01;
  if (isNaN(tax_amount)) {
    tax_amount = 0;
  }

  let total = subtotal + tax_amount;

  $('#subtotal-amount').html(
    accounting.formatMoney(subtotal, { precision: 0 })
  );
  $('#tax-amount').html(accounting.formatMoney(tax_amount, { precision: 0 }));
  $('#total-amount').html(accounting.formatMoney(total, { precision: 0 }));
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

  $('#tax-input').keyup(() => {
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

  // TODO: CATCH ERROR WHEN INPUT DOESNT MATCH SITE
  let product_url;
  if (window.location.pathname.includes('edit-quote')) {
    product_url = `../product/${pn}`;
  } else if (window.location.pathname.includes('create-quote')) {
    product_url = `product/${pn}`;
  }

  fetch(product_url)
    .then((response) => response.json())
    .then((data) => {
      $(tr).find('.product-title').html(data['title']);
      $(tr).find('.product-brand').html(`Brand: ${data['brand']}`);
      $(tr).find('.product-description').html(data['description']);
    });
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

  // TODO: DELETE VALUES IN NEW LINE BEFORE APPENDING

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
