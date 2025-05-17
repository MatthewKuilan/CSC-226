function whoami() {
    const wallet = document.querySelector("input[name='wallet-question']:checked");
    const bully = document.querySelector("input[name='bully-question']:checked");
    const challenge = document.querySelector("input[name='challenge-question']:checked");
    const game = document.querySelector("input[name='game-question']:checked");
    const motivation = document.querySelector("input[name='motivation-question']:checked");

    if (wallet && bully && challenge && game && motivation) {
        let house_results = {
            "Hufflepuff": (wallet.value == "wallet-a") + (bully.value == "bully-b") + (challenge.value == "challenge-b") + (game.value == "game-a") + (motivation.value == "motivation-b"),
            "Gryffindor": (wallet.value == "wallet-b") + (bully.value == "bully-a") + (challenge.value == "challenge-a") + (game.value == "game-b") + (motivation.value == "motivation-a"),
            "Ravenclaw" : (wallet.value == "wallet-c") + (bully.value == "bully-c") + (challenge.value == "challenge-c") + (game.value == "game-c") + (motivation.value == "motivation-c"),
            "Slytherin" : (wallet.value == "wallet-d") + (bully.value == "bully-d") + (challenge.value == "challenge-d") + (game.value == "game-d") + (motivation.value == "motivation-d"),
        };

        var house_max = 0;
        var house_name = "";
        for (let house in house_results) {
            if (house_max <= house_results[house]) {
                house_max = house_results[house];
                house_name = house;
            }
        }

        // Create form data to submit
        const formData = new FormData();
        formData.append('wallet_choice', wallet.value);
        formData.append('bully_choice', bully.value);
        formData.append('challenge_choice', challenge.value);
        formData.append('game_choice', game.value);
        formData.append('motivation_choice', motivation.value);
        formData.append('house', house_name);
        
        // Reset radio buttons
        wallet.checked = false;
        bully.checked = false;
        challenge.checked = false;
        game.checked = false;
        motivation.checked = false;

        // Show result in dialog
        const dialog = document.getElementById("whoami-dialog");
        dialog.innerHTML = ''; // Clear previous content
        
        let text = document.createElement('p');
        text.appendChild(document.createTextNode('Congrats!!! You are a ${house_name}'));
        dialog.appendChild(text);

        // Add buttons to dialog
        let saveButton = document.createElement('button');
        saveButton.style = "width: 45%; margin-right: 5%";
        saveButton.appendChild(document.createTextNode("Save Result"));
        saveButton.onclick = function() {
            // Send data to server
            fetch('/save_quiz_result', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Your quiz results have been saved!');
                    if (data.redirect) {
                        window.location.href = data.redirect;
                    }
                } else {
                    alert('Error saving results: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while saving your results.');
            });
            dialog.close();
        };
        dialog.appendChild(saveButton);

        let cancelButton = document.createElement('button');
        cancelButton.style = "width: 45%";
        cancelButton.appendChild(document.createTextNode("Close"));
        cancelButton.onclick = function() {
            dialog.close();
        };
        dialog.appendChild(cancelButton);

        dialog.showModal();
    } else {
        alert("Please answer all questions to get your result!");
    }
}