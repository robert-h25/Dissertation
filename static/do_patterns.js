// IF user presses generate_puzzle button
document.getElementById("get_patterns").addEventListener("click", function() {
    //Trigger get_patterns view
    fetch('/generate_patterns',{method: 'POST'}) 
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server
            console.log("Patterns:", data.patterns);
            console.log("Score:", data.score);
            // If we recieve data display it
            if (data.patterns.length > 0) {
                display_data(data.patterns,data.score);
            } else {
                console.log("No patterns found.");
            }
            
        })
        .catch(error => {
            console.error(error);
        });
        
});

// TODO: format the data for the display
// Function to display the patterns and score
function display_data(patterns, score) {
    const patternsCon = document.getElementById("patterns");
    patternsCon.innerHTML = ""; 

    //list of all pattern names in this order
    const patternNames = [
        "Sole Technique",
        "Unique Candidate",
        "BRC Interaction",
        "Block-Block Interaction",
        "Naked Subset",
        "Hidden Subset",
        "X-Wing",
        "Swordfish",
        "Forcing Chain",
        "XY-Wing",
        "Unique Rectangle"
    ];

    // add patterns
    patterns.forEach((value, index) => {
        const patternDiv = document.createElement("div"); // Create a new div element for each pattern
        patternDiv.classList.add("pattern"); // Add the "pattern" class to the div
        // get name and display data for each
        patternDiv.innerHTML = `<strong>${patternNames[index]}:</strong> occurs ${value.length} times`;
        // add to the patternsCon div
        patternsCon.appendChild(patternDiv);
    });

    // add score
    const scoreDiv = document.createElement("div"); // Create a new div element for the score
    scoreDiv.innerHTML = `<strong>Score:</strong> ${score}`;
    // Add the scoreDiv to the patternsCon div
    patternsCon.appendChild(scoreDiv);

    // more details line
    const moreDetails = document.createElement("div");
    moreDetails.innerHTML = "Look at the command line for more details!";
    patternsCon.appendChild(moreDetails);
}