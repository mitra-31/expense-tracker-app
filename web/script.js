

function add()
{
    amount = document.getElementById("amount").value;
    desc = document.getElementById("desc").value;
    eel.add_amount(amount,desc)(callback);
}


function table_create(data) {
    tablerow = document.getElementById("table-body");
    create_row = document.createElement("tr");
    var amount = create_row.insertCell();
    var date = create_row.insertCell();
    var time = create_row.insertCell();
    var desc = create_row.insertCell();
    amount.innerHTML = data["amount"];
    date.innerHTML = data["date"];
    time.innerHTML = data["time"];
    desc.innerHTML = data["desc"];
    create_row.append(amount);
    create_row.append(date);
    create_row.append(time);
    create_row.append(desc);
    tablerow.append(create_row);
} 



function createchart()
{
    eel.create()(img)
}

function img(base64)
{
    document.getElementById("img").src = base64;
}


function createtable(){
    fetch("tracker.json")
        .then(response => response.json())
        .then(data => {
            for (i in data)
                table_create(data[i])
        })
}
createtable();
