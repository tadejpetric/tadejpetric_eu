function create_cell(type, attributes) {
    let cell = document.createElement('td');
    let contents = document.createElement(type);
    for (let key in attributes) {
        contents.setAttribute(key, attributes[key]);
    }
    cell.appendChild(contents);
    return cell;
}


function append_row() {
    let table = document.getElementById('contents').getElementsByTagName('tbody')[0];
    let row_count = table.getElementsByTagName("tr").length;
    let row = document.createElement('tr');
    
    // create inputs
    row.appendChild(create_cell('input', {'name': 'opravilo', 'type': 'text'}));
    row.appendChild(create_cell('input', {'name': 'me', 'type': 'text'}));
    row.appendChild(create_cell('input', {'name': 'evro_kol',
                                          'type': 'number',
                                          'step': '0.01',
                                          'oninput': 'calculate_result('+row_count+');'}));
    row.appendChild(create_cell('input', {'name': 'kol',
                                          'type': 'number',
                                          'step': '0.0001',
                                          'oninput': 'calculate_result('+row_count+');'}));
    row.appendChild(create_cell('span', {}));
    
    let but = create_cell('button', {'type': 'button', 'onclick': 'delete_row('+row_count+');'});
    but.getElementsByTagName('button')[0].innerHTML = 'Odstrani';
    row.appendChild(but);

    table.appendChild(row);
}

function calculate_result(row_number) {
    let row = document.getElementById('contents').getElementsByTagName('tbody')[0].getElementsByTagName('tr')[row_number].getElementsByTagName('td');
    let first_value = Number(row[2].children[0].value);
    let second_value = Number(row[3].children[0].value);
    let total = first_value * second_value;
    
    row[4].children[0].innerText = total.toFixed(2);
    let sum_val = 0;
    for (let element of document.getElementById('contents').getElementsByTagName('tbody')[0].children) {
        sum_val += Number(element.getElementsByTagName('td')[4].children[0].innerText);
    }
    document.getElementById('contents').getElementsByTagName('tfoot')[0].children[0].getElementsByTagName('td')[2].innerText = sum_val.toFixed(2) + " €";
}

function delete_row(row_number) {
    document.getElementById('contents').getElementsByTagName('tbody')[0].deleteRow(row_number);
    let i = 0;
    for (let row of document.getElementById('contents').getElementsByTagName('tbody')[0].children) {
        row.getElementsByTagName('td')[2].children[0].setAttribute('oninput', 'calculate_result('+i+');');
        row.getElementsByTagName('td')[3].children[0].setAttribute('oninput', 'calculate_result('+i+');');
        row.getElementsByTagName('td')[4].children[0].setAttribute('onclick', 'delete_row('+i+');');
    }
    calculate_result(0);
}
