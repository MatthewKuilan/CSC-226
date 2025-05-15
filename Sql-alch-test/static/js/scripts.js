function whoami() {
    const wallet = document.querySelector("input[name='wallet-question']:checked");
    const bully = document.querySelector("input[name='bully-question']:checked");
    const challenge = document.querySelector("input[name='challenge-question']:checked");
    const game = document.querySelector("input[name='game-question']:checked");
    const motivation = document.querySelector("input[name='motivation-question']:checked");

    if (wallet && bully && challenge && game && motivation) {
        wallet.checked = false;
        bully.checked = false;
        challenge.checked = false;
        game.checked = false;
        motivation.checked = false;

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

        const dialog = document.getElementById("whoami-dialog");
        let text = document.createElement('p');
        text.appendChild(document.createTextNode(`Congrats!!! You are a ${house_name}`));
        dialog.appendChild(text);

        let exit = document.createElement('button');
        exit.style = "width: 30%; margin-left: 35%; margin-right: 35%"
        exit.appendChild(document.createTextNode("Ok"));
        dialog.appendChild(exit);

        dialog.showModal();
    } else {
        // TODO Go to error
    }
}