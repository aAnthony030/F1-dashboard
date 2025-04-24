const sessions = ["FP1", "FP2", "FP3", "Q", "R"]
let currentSessionIndex = sessions.indexOf("R");

document.getElementById("prevSession").addEventListener("click", () => {
    if (currentSessionIndex > 0) {
        currentSessionIndex--;
        updateSession();
    }
    else {
        currentSessionIndex = 4;
    }
});

document.getElementById("nextSession").addEventListener("click", () => {
    if (currentSessionIndex < sessions.length - 1) {
        currentSessionIndex++;
        updateSession();
    }
    else {
        currentSessionIndex = 0;
    };
});


function updateSession() {
    const sessionType = sessions[currentSessionIndex];
    const year = document.getElementById("year").value;
    const track = document.getElementById("track").value;

    window.location.href = `/get_track_data?year=${year}&track=${track}&session=${sessionType}`;
}

