document.addEventListener('DOMContentLoaded', function () {
  let new_quote_button = $('#new_quote_button');

  if (new_quote_button) {
    new_quote_button.click(() => (location.href = 'create-quote'));
  }

  $('#price, #qty, #discount').keyup(() => updateAmount());

  $('.datepicker').datepicker();
  console.log('Document loaded!');
});

function updateAmount() {
  let amount = $('#amount-column');
  let qty = $('#qty').val();
  let price = $('#price').val();
  let discount = $('#discount').val();

  amount.html((qty * price * (100 - discount)) / 100);

  console.log(amount.html(), qty, price, discount);
}
