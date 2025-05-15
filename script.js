function getBotResponse(input) {
  const responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Need any EdTech assistance?",
    "bye": "Goodbye! Have a great day.",
    "thanks": "You're welcome!",
    "course": "You can check the course schedule in your portal.",
    "default": "Sorry, I didn't understand that. Can you try again?"
  };

  for (let key in responses) {
    if (input.includes(key)) {
      return responses[key];
    }
  }
  return responses["default"];
}

function sendMessage() {
  const input = document.getElementById("user-input").value;
  const chatBox = document.getElementById("chat-box");

  chatBox.innerHTML += `<p><strong>You:</strong> ${input}</p>`;

  const botReply = getBotResponse(input.toLowerCase());
  chatBox.innerHTML += `<p><strong>Bot:</strong> ${botReply}</p>`;

  document.getElementById("user-input").value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}