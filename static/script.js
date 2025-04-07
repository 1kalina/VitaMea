var markdownView = document.createElement("github-md");
const toggleBtn = document.getElementById('toggle-btn');
const editor = document.getElementById('editor');
const container = document.getElementById('container');
let isEditing = false;

editor.value = `# Hello Markdown
        
        This is a simple markdown editor.
        
        - Edit by clicking the button
        - View the rendered markdown
        - Enjoy!`;
function setEditMode() {
    // Switch to edit mode
    toggleBtn.textContent = 'View';
    editor.style.display = 'block';
    editor.value = editor.value;
    markdownView.remove();
}
function setReadMode() {
    // Switch to view mode

    // TODO: Save locally

    markdownView = document.createElement("github-md");
    toggleBtn.textContent = 'Edit';
    markdownView.textContent = editor.value;
    markdownView.style.display = 'block';
    editor.style.display = 'none';
    container.appendChild(markdownView);
    renderMarkdown();
}
toggleBtn.addEventListener('click', () => {
    isEditing = !isEditing;

    if (isEditing) {
        setEditMode();

    } else {
        setReadMode();
    }
});

setReadMode();