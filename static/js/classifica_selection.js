document.getElementById("btnPiloti").addEventListener("click", function() {
    document.getElementById("tabellaPiloti").style.display = "table";
    document.getElementById("tabellaTeam").style.display = "none";
    this.classList.add("btn-primary");
    this.classList.remove("btn-secondary");
    document.getElementById("btnTeam").classList.remove("btn-primary");
    document.getElementById("btnTeam").classList.add("btn-secondary");
});


document.getElementById("btnTeam").addEventListener("click", function() {
    document.getElementById("tabellaTeam").style.display = "table";
    document.getElementById("tabellaPiloti").style.display = "none";
    this.classList.add("btn-primary");
    this.classList.remove("btn-secondary");
    document.getElementById("btnPiloti").classList.remove("btn-primary");
    document.getElementById("btnPiloti").classList.add("btn-secondary");
});

