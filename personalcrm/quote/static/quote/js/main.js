document.addEventListener('DOMContentLoaded', function () {
  let new_quote_button = $('#new_quote_button');

  if (new_quote_button) {
    new_quote_button.click(() => (location.href = 'create-quote'));
  }

  $('.price, .qty, .discount').keyup((event) => {
    let tr = event.target.closest('tr');
    updateAmount(tr);
  });

  $('.deleteRowButton').click((event) => {
    let tr = event.target.closest('tr');
    deleteRow(tr);
  });

  $('#new-item').click(() => addNewLine());

  $('.hiddenCheck').click((event) => {
    let checkbox = event.target;
    let tr = event.target.closest('tr');
    hideRow(tr, checkbox);
  });

  $('.datepicker').datepicker();
  console.log('Document loaded!');
});

function updateAmount(tr) {
  let qty = $(tr).find('.qty').val();
  let price = $(tr).find('.price').val();
  let discount = $(tr).find('.discount').val();

  let amount = (qty * price * (100 - discount)) / 100;

  $(tr).find('.amount').html(amount);
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
    '                                <select class="form-control" id="companySelect">' +
    `                                ${products}` +
    '                                </select>' +
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
    // '                            <div>%</div>' +
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
