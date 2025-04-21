document.getElementById("trackSelect").addEventListener("change", function() {
    const track = this.value;
    const yearSelect = document.getElementById("yearSelect");
        
    if (!track) {
        yearSelect.innerHTML = '<option>-- Scegli prima una pista --</option>';
        yearSelect.disabled = true;
        return;
    }

    fetch("/get_years", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ track: track })
    })
    .then(response => response.json())
    .then(years => {
        yearSelect.disabled = false;
        yearSelect.innerHTML = '<option value="">-- Seleziona un anno --</option>';
        years.forEach(year => {
            const option = document.createElement("option");
            option.value = year;
            option.textContent = year;
            yearSelect.appendChild(option);
        });
    });
});