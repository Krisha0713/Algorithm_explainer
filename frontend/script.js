let utterance = null;

async function explainConcept() {
    const text = document.getElementById("inputText").value;
    const level = document.getElementById("level").value;

    const res = await fetch("http://127.0.0.1:5000/explain", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, level })
    });

    const data = await res.json();

    document.getElementById("definition").innerText = data.definition || "";
    document.getElementById("analogy").innerText = data.analogy || "";
    document.getElementById("example").innerText = data.engineering_example || "";

    const diagramDiv = document.getElementById("diagram");
    diagramDiv.innerHTML = data.diagram || "";

    if (data.diagram) {
        mermaid.init(undefined, diagramDiv);
    }
}

function playVoice() {
    stopVoice();

    const speed = document.getElementById("voiceSpeed").value;

    const text =
        "Definition. " + document.getElementById("definition").innerText +
        ". Analogy. " + document.getElementById("analogy").innerText +
        ". Engineering example. " + document.getElementById("example").innerText;

    utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = speed;

    speechSynthesis.speak(utterance);
}

function pauseVoice() {
    speechSynthesis.pause();
}

function stopVoice() {
    speechSynthesis.cancel();
}





