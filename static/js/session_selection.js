const sessions = ["FP1", "FP2", "FP3", "SQ", "S", "Q", "R"];

function getCurrentSessionFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const sessionParam = urlParams.get('session');
    const index = sessions.indexOf(sessionParam);
    return index !== -1 ? index : sessions.indexOf("R"); // Default to "R" if not found
}

let currentSessionIndex = getCurrentSessionFromURL();

document.getElementById("prevSession").addEventListener("click", () => {
    if (currentSessionIndex > 0) {
        currentSessionIndex--;
    } else {
        currentSessionIndex = sessions.length - 1; // Go to last item
    }
    updateSession();
});

document.getElementById("nextSession").addEventListener("click", () => {
    if (currentSessionIndex < sessions.length - 1) {
        currentSessionIndex++;
    } else {
        currentSessionIndex = 0; // Go to first item
    }
    updateSession();
});

function updateSession() {
    const sessionType = sessions[currentSessionIndex];
    const year = document.getElementById("year").value;
    const track = document.getElementById("track").value;

    window.location.href = `/get_track_data?year=${year}&track=${track}&session=${sessionType}`;
}