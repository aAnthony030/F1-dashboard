fetch('/api/grafico-posizioni')
    .then(res => res.json())
    .then(data => {
        let traces = [];

        for (const [driver, values] of Object.entries(data)) {
            traces.push({
                x: values.x,
                y: values.y,
                name: driver,
                mode: 'lines+markers',
                type: 'scatter'
            });
        }

        const layout = {
            yaxis: {
                autorange: 'reversed',
                title: 'Posizione'
            },
            xaxis: {
                title: 'Giro'
            },
            margin: {
                t: 30
            },
            legend: {
                orientation: "h"
            },
        };

        Plotly.newPlot('grafico-posizioni', traces, layout, {
            responsive: true
        });
    });