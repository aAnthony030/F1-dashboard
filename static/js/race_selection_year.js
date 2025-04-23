// Primo blocco: aggiorna le piste quando si seleziona l'anno
document.getElementById("yearSelect").addEventListener("change", function() {
    const year = this.value;
    const trackSelect = document.getElementById("trackSelect");
        
    if (!year) {
        trackSelect.innerHTML = "<option value=''>-- Scegli prima un anno --</option>";
        trackSelect.disabled = true;
        return;
    }

    fetch("/get_tracks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ year: year })
    })
    .then(response => response.json())
    .then(tracks => {
        trackSelect.disabled = false;
        trackSelect.innerHTML = '<option value="">-- Seleziona una pista --</option>';
        tracks.forEach(track => {  // 
            const option = document.createElement("option");
            option.value = track;
            option.textContent = track;
            trackSelect.appendChild(option);
        });
    })
    .catch(error => {
        console.error("Errore nel caricamento delle piste:", error);
        alert("Errore nel caricamento delle piste.");
    });
});


// Secondo blocco: invia pista + anno selezionati a Flask per ottenere i dati
document.getElementById("mostraDati").addEventListener("click", function(e) {
    e.preventDefault();

    const track = document.getElementById("trackSelect").value;
    const year = document.getElementById("yearSelect").value;

    if (!track || !year) {
        alert("⚠️ Devi selezionare sia anno che pista.");
        return;
    }

    // Redirect con i dati come query string
    window.location.href = `/get_track_data?track=${encodeURIComponent(track)}&year=${encodeURIComponent(year)}`;
});
