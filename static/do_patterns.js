// IF user presses generate_puzzle button
document.getElementById("get_patterns").addEventListener("click", function() {
    //Trigger get_patterns view
    fetch('/generate_patterns',{method: 'POST'}) 
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server
            console.log(data);
        })
        .catch(error => {
            console.error(error);
        });
        
});