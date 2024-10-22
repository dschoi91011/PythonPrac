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