const noRefresh = (e) => {
    e.preventDefault();
};
function downloadNote() {
    var topic = document.querySelector('#topic').value;
    var classNotesContent = document.querySelector('.generated-notes').innerText;

    // Create a new jsPDF instance
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Add the title at the top of the PDF
    doc.setFontSize(16);
    doc.text(topic + ' Notes', 10, 10);

    // Set the font size for the notes content
    doc.setFontSize(12);

    // Add the content with word wrap
    var splitContent = doc.splitTextToSize(classNotesContent, 180); // 180 is the max width in mm
    doc.text(splitContent, 10, 20); // Start text at x: 10, y: 20

    // Save the generated PDF with the topic as the filename
    doc.save(`${topic}notes.pdf`);
}



const openNotes = () => {
    document.querySelector("#music").style.display = "none";
    document.querySelector("#notes").style.display = "grid";
}
const openMusic = () => {
    document.querySelector("#notes").style.display = "none";
    document.querySelector("#music").style.display = "grid";
}