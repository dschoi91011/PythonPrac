const generateNotes = () => {
    const localStorage = window.localStorage;
    let notes = localStorage.getItem('notes') ? JSON.parse(localStorage.getItem('notes')) 
    : 
    { 
        "1634359781154": {
            "text": "Welcome to Tiny Notes! Your notes will remain unless you clear your browser's local storage or click 'remove' down below.", 
            "id": 1634359781154
        }
    }
};


const formatNote = note => {
    let noteModule = document.createElement('div');
    noteModule.className = 'note-module';
    let noteText = document.createElement('span');
    let noteSegment = document.createElement('div');
    noteSegment.className = 'note-segment';
    let date = document.createElement('span');
    let remove = document.createElement('button');
    remove.className = 'remove';
    remove.style.color = '#FFAB00';
    remove.innerHTML = 'remove';
    remove.onclick = () => removeNote(note.id);
 
    noteText.innerHTML = note.text;
    date.innerHTML = new Date(note.id).toDateString();
 
    noteSegment.append(date);
    noteSegment.append(remove);
    noteModule.append(noteText);
    noteModule.append(noteSegment);
 
    return noteModule;
 };


 const renderNotes = () => {
    notebook.innerHTML = ''; // Clear previous notes
    Object.values(notes).reverse().forEach(note => {
       let formattedNote = formatNote(note);
       notebook.append(formattedNote); // Add each formatted note to the notebook
    });
 };


 const addNote = text => {
    const note = {
      text: text,
      id: Date.now(),
    };
    notes[note.id] = note;
    localStorage.setItem('notes', JSON.stringify(notes)); // Save to local storage
    let formattedNote = formatNote(note);
    notebook.prepend(formattedNote); // Add the new note to the top
 };


 const removeNote = id => {
    delete notes[id]; // Remove the note from the notes object
    localStorage.setItem('notes', JSON.stringify(notes)); // Update local storage
    renderNotes(); // Re-render the remaining notes
 };