// JS script to get and display the puzzle

// IF user presses generate_puzzle button
document.getElementById("generate_puzzle").addEventListener("click", function() {
    //Trigger generate_puzzle view
    fetch('/generate_puzzle', { method: 'POST' })
        // convert response from json to JS
        .then(response => response.json())
        .then(data => {
            // get Table
            const table = document.getElementById("table");
            // clear previous table displayed
            table.innerHTML = ""; 
            const patternsCon = document.getElementById("patterns");
            patternsCon.innerHTML = ""; 
            const grid = data.grid;
            //display grid
            grid.forEach(rowData => {
                const row = document.createElement("tr");
                rowData.forEach(cellData => {
                    const cell = document.createElement("td");
                    // display number for the cell based on number in cell
                    if (cellData === 0) {
                        cell.textContent = "";
                    } else {
                        cell.textContent = cellData;
                    }
                    //append cell to row
                    row.appendChild(cell);
                });
                //append row to table
                table.appendChild(row);
            });
        })
        // catch errors
        .catch(error => console.error('Error:', error));
});