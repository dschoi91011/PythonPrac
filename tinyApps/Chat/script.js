const generateChat = () => {
    // Create the chat history container
    const chatHistory = document.createElement('div');
    chatHistory.id = 'chat-history';
    chatHistory.style.border = '5px solid #FDD835';

    // Create the form for adding new messages
    const chatForm = document.createElement('form');
    chatForm.id = 'chat-form';

    // Input field for user message
    const userInput = document.createElement('input');
    userInput.id = 'user-input';
    userInput.placeholder = 'Ask me anything...';

    // Submit button
    const sendMsg = document.createElement('button');
    sendMsg.id = 'send-message';
    sendMsg.type = 'submit';
    sendMsg.innerHTML = 'Send';
    sendMsg.style.color = '#FDD835';

    // Append input field and button to form
    chatForm.append(userInput);
    chatForm.append(sendMsg);

    // Append chat history and form to the main display
    const options = document.getElementById('options');
    const display = document.getElementById('display');
    display.append(chatHistory);
    options.append(chatForm);

    document.getElementById('profile').style.color = `#FDD835`;
};

let chatMessages = []; // To store all chat messages

// Add a new message to the chat
const addMessage = (text, sender) => {
    chatMessages.push({ text, sender }); // Add the message to the chat history
    renderChat(); // Re-render the chat window
};

// Handle form submission
chatForm.addEventListener('submit', async e => {
    e.preventDefault(); // Prevent the page from reloading
    const userMessage = userInput.value.trim(); // Get the user's message

    if (userMessage === '') return; // Do nothing if the input is empty
    addMessage(userMessage, 'user'); // Add user message to chat
    userInput.value = ''; // Clear the input field

    const aiResponse = await fetchAIResponse(userMessage); // Fetch the AI's response
    addMessage(aiResponse, 'ai'); // Add AI response to chat
});

const fetchAIResponse = async (message) => {
    try {
        const response = await fetch('https://api.openai.com/v1/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer YOUR_API_KEY`
            },
            body: JSON.stringify({
                model: 'text-davinci-003',
                prompt: message,
                max_tokens: 150
            })
        });

        const data = await response.json(); // Parse the response
        return data.choices[0].text.trim(); // Return the AI’s response
    } catch (error) {
        console.error('Error fetching AI response:', error);
        return 'Sorry, something went wrong. Please try again later.';
    }
};